import discord
import asyncio
import random
from selenium import webdriver, common
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from PIL import Image
from io import BytesIO
from random import randint
import time

url_server = 'https://discord.com/channels/<id_channel>'
players = {}
browser = None
logged = False

def browser_firefox():
    # start web browser
    options = Options()
    options.set_preference("media.navigator.permission.disabled", True)
    options.set_preference("permissions.fullscreen.allowed", True)
    options.set_preference("browser.fullscreen.autohide", True)
    options.set_preference("browser.fullscreen.animateUp", 0)
    return webdriver.Firefox(executable_path="geckodriver", options=options)

client = discord.Client()

@client.event
async def on_ready():
    print('BOT ONLINE - OLÁ MUNDO')
    print(client.user.name)
    print(client.user.id)
    print('-----BR------')

@client.event
async def on_message(message):
    global browser
    global logged
    if message.content.startswith('-start'):
        channel = message.channel
        await channel.send('Aquecendo o projetor...')
        browser = browser_firefox()
        browser.maximize_window()
        browser.fullscreen_window()
        browser.get(url_server)
        time.sleep(5)
        if not logged:
            element = browser.find_element_by_xpath("//div[contains(@class, 'qrLoginInner')]")
            location = element.location
            size = element.size
            png = browser.get_screenshot_as_png() # saves screenshot of entire page

            im = Image.open(BytesIO(png)) # uses PIL library to open image in memory

            left = location['x'] + 150
            top = location['y'] + 50
            right = location['x'] + 200 + size['width'] + 50
            bottom = location['y'] + size['height'] + 130

            im = im.crop((left, top, right, bottom)) # defines crop points
            im.save('qrcode.png') # saves new cropped image
            with open('qrcode.png', 'rb') as f:
                picture = discord.File(f)
                await channel.send(file=picture)

            while not logged:
                try:
                    browser.find_element_by_xpath("//div[contains(@class, 'qrLoginInner')]")
                except:
                    await channel.send('Login feito!')
                    await channel.send('Conectando...')
                    logged = True
                    time.sleep(5)
                    browser.execute_script("document.getElementById('channels').scrollTo(0, 1000);")
                    time.sleep(1)
                    browser.find_element_by_xpath("//div[contains(@class, 'channelName') and contains(., 'Cineminha')]").click()
                    time.sleep(1)
                    browser.find_element_by_xpath("//button[contains(., 'Screen')]").click()
                    time.sleep(1)
                    browser.execute_script("window.open('');")
                    browser.switch_to.window(browser.window_handles[1])
                    await channel.send('Pronto pra você!')
                
        else:
            await channel.send('Login já realizado!')
    if message.content.startswith('-stop'):
        channel = message.channel
        browser.execute_script("window.close();")
        browser.close()
        logged = False
        await channel.send('Até a proxima cessão!')
    if message.content.startswith('-cine'):
        channel = message.channel
        
        if logged:
            await channel.send('Bora um cineminha?!')

            link = message.content.split(" ")[1]
            browser.get(link)

            def check(reaction, user):
                return user == message.author and str(reaction.emoji) == '\N{THUMBS UP SIGN}'

            try:
                reaction, user = await client.wait_for('reaction_add', timeout=60.0, check=check)
            except asyncio.TimeoutError:
                print('esperando')
            else:
                await channel.send('\N{THUMBS UP SIGN}')
        else:
            await channel.send('Faça o login')
    if message.content.startswith('-play'):
        channel = message.channel
        
        if logged:
            browser.find_element_by_xpath('/html/body').send_keys(Keys.SPACE)
        else:
            await channel.send('Faça o login')
    if message.content.startswith('-fullscreen'):
        channel = message.channel
        
        if logged:
            browser.find_element_by_xpath('/html/body').send_keys('f')
        else:
            await channel.send('Faça o login')

client.run('Token_bot') #https://discord.com/developers/applications