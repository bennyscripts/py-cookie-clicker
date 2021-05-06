# cookie clicker in tkinter
import tkinter as tk
import os
import pygame
import pyglet
from tkinter.ttk import *
from tkinter import *
from PIL import Image, ImageTk

def resource_path(relative_path):
  try:
    base_path = sys._MEIPASS
  except Exception:
    base_path = os.path.abspath(".")

  return os.path.join(base_path, relative_path)

windowWidth = 300
windowHeight = 300

cookieCount = 72
upgrade = ""
increment = 200

grannyPrice = 100
grannyLevel = 0
maxGrannyLevel = 1000
grannyEnabled = False
grannySpeed = 1000
grannyCookies = 1

# animatedLabelY = 350
# animatedLabelX = 120

song = resource_path("music/song.mp3")
songVolume = 0.75
songPlaying = True

sfxPlaying = True

def quitApp(event):
  app.destroy()

def checkSong():
  if songPlaying is True:
    pygame.mixer.music.set_volume(songVolume)
    canvas.itemconfig(menuText1, text="Song Playing")
    canvas.itemconfig(menuText1Stroke, text="Song Playing")
  else:
    pygame.mixer.music.set_volume(0.0)
    canvas.itemconfig(menuText1, text="Song Muted")
    canvas.itemconfig(menuText1Stroke, text="Song Muted")

  if sfxPlaying is True:
    canvas.itemconfig(menuText2, text="SFX Playing")
    canvas.itemconfig(menuText2Stroke, text="SFX Playing")
  else:
    canvas.itemconfig(menuText2, text="SFX Muted")
    canvas.itemconfig(menuText2Stroke, text="SFX Muted")

  app.after(1, checkSong)

def updateCookieCountLabel():
  if cookieCount == 1:
    canvas.itemconfig(cookieCountLabel, text=f"{cookieCount:,} cookie")
    canvas.itemconfig(cookieCountLabelStroke, text=f"{cookieCount:,} cookie")
  else:
    canvas.itemconfig(cookieCountLabel, text=f"{cookieCount:,} cookies")
    canvas.itemconfig(cookieCountLabelStroke, text=f"{cookieCount:,} cookies")

  app.after(1, updateCookieCountLabel)

# def animateLabel():
#   global animatedLabelY
#   global animatedLabelX
#
#   if grannyEnabled is True or upgrade != "plus1":
#     animatedLabelY += -10
#     animatedLabelX += 5
#
#     if animatedLabelY == -10:
#       animatedLabelY = 350
#
#     if animatedLabelX == 135:
#       animatedLabelX = 125
#
#     canvas.itemconfig(upgradeLabel, text=upgrade.replace("plus", "+"))
#     canvas.coords(upgradeLabel, (animatedLabelX + 15, animatedLabelY))
#
#     canvas.itemconfig(upgradeLabelStroke, text=upgrade.replace("plus", "+"))
#     canvas.coords(upgradeLabelStroke, (animatedLabelX + 15 + 2, animatedLabelY + 1))
#
#   app.after(75, animateLabel)

def hidePurchaseLabel():
  canvas.itemconfig(purchaseLabel, text="")
  canvas.itemconfig(purchaseLabelStroke, text="")
  canvas.coords(purchaseLabelBackground, -10, -10, -10, -10)

def buyGranny(event):
  if sfxPlaying is True:
    clickSound = pygame.mixer.Sound(resource_path('audio/click.mp3')).play()

  global cookieCount
  global grannyPrice
  global grannyLevel
  global grannyEnabled
  global grannySpeed
  global grannyCookies

  if cookieCount >= grannyPrice:
    if grannyEnabled is True:
      if grannyLevel == maxGrannyLevel:

        canvas.itemconfig(purchaseLabel, text=f"You cant purchase\nanymore Grandmas.")
        canvas.itemconfig(purchaseLabelStroke, text=f"You cant purchase\nanymore Grandmas.")

        canvas.coords(purchaseLabelBackground, windowHeight, 0, 0, windowWidth)

        if sfxPlaying is True:
          clickSound = pygame.mixer.Sound(resource_path('audio/snarl.mp3')).play()

        app.after(1000, hidePurchaseLabel)

      else:
        cookieCount = cookieCount - grannyPrice

        grannyPrice += 25
        grannyLevel += 1
        grannyCookies += 1

        canvas.itemconfig(buyGrannyBtn, text=f"Buy a Grandma ({grannyPrice:,})\nYou have {grannyLevel} grandmas.")
        canvas.itemconfig(buyGrannyBtnStroke, text=f"Buy a Grandma ({grannyPrice:,})\nYou have {grannyLevel} grandmas.")

        canvas.itemconfig(purchaseLabel, text=f"Purchased a\nnew Grandma")
        canvas.itemconfig(purchaseLabelStroke, text=f"Purchased a\nnew Grandma")

        canvas.coords(purchaseLabelBackground, windowHeight, 0, 0, windowWidth)

        if sfxPlaying is True:
          clickSound = pygame.mixer.Sound(resource_path('audio/buy.mp3')).play()

        app.after(1000, hidePurchaseLabel)

    else:
      grannyEnabled = True
      cookieCount = cookieCount - grannyPrice

      grannyPrice += 25
      grannyLevel += 1

      canvas.itemconfig(buyGrannyBtn, text=f"Buy a Grandma ({grannyPrice:,})\nYou have {grannyLevel} grandmas.")
      canvas.itemconfig(buyGrannyBtnStroke, text=f"Buy a Grandma ({grannyPrice:,})\nYou have {grannyLevel} grandmas.")

      canvas.itemconfig(purchaseLabel, text=f"Purchased a\nnew Grandma")
      canvas.itemconfig(purchaseLabelStroke, text=f"Purchased a\nnew Grandma")

      canvas.coords(purchaseLabelBackground, windowHeight, 0, 0, windowWidth)

      if sfxPlaying is True:
        clickSound = pygame.mixer.Sound(resource_path('audio/buy.mp3')).play()

      app.after(1000, hidePurchaseLabel)
  else:
    canvas.itemconfig(purchaseLabel, text="Not enough cookies")
    canvas.itemconfig(purchaseLabelStroke, text="Not enough cookies")
    canvas.coords(purchaseLabelBackground, windowHeight, 0, 0, windowWidth)

    if sfxPlaying is True:
      clickSound = pygame.mixer.Sound(resource_path('audio/snarl.mp3')).play()

    app.after(1000, hidePurchaseLabel)

def granny():
  global cookieCount
  global upgrade

  if grannyEnabled is True:
    cookieCount += grannyCookies

  app.after(grannySpeed, granny)

def resetCookieBtn():
  global cookie2

  cookie2 = ImageTk.PhotoImage(Image.open(resource_path("assets/cookie.png")).resize((165, 165), Image.ANTIALIAS))
  canvas.itemconfig(cookieBtn, image=cookie2)

def addCookie(event):
  global cookieCount
  global cookie2
  cookieCount += 1

  if sfxPlaying is True:
    clickSound = pygame.mixer.Sound(resource_path('audio/clickb7.mp3')).play()

  cookie2 = ImageTk.PhotoImage(Image.open(resource_path("assets/cookie.png")).resize((160, 160), Image.ANTIALIAS))
  canvas.itemconfig(cookieBtn, image=cookie2)
  app.after(50, resetCookieBtn)

def buyGrannyBtnHoverEnter(event):
  canvas.itemconfig(buyGrannyBtnStroke, fill="black")
  canvas.itemconfig(buyGrannyBtn, fill="white")


def buyGrannyBtnHoverLeave(enter):
  canvas.itemconfig(buyGrannyBtnStroke, fill="black")
  canvas.itemconfig(buyGrannyBtn, fill="white")

def openMenu(event):
  if sfxPlaying is True:
    clickSound = pygame.mixer.Sound(resource_path('audio/click.mp3')).play()
  canvas.coords(purchaseLabelBackground, windowHeight, 0, 0, windowWidth)
  canvas.coords(menuText1Stroke, (windowWidth / 2 + 2, windowHeight / 2 + -50 + 2))
  canvas.coords(menuText1, (windowWidth / 2, windowHeight / 2 + -50))
  canvas.coords(menuText2Stroke, (windowWidth / 2 + 2, windowHeight / 2 + 2))
  canvas.coords(menuText2, (windowWidth / 2, windowHeight / 2))
  canvas.coords(menuText3Stroke, (windowWidth / 2 + 2, windowHeight / 2 + 50 + 2))
  canvas.coords(menuText3, (windowWidth / 2, windowHeight / 2 + 50))
  canvas.coords(menuBtn, (windowWidth - 20, 500))
  canvas.coords(closeMenuBtn, (windowWidth - 20, 20))

def closeMenu(event):
  if sfxPlaying is True:
    clickSound = pygame.mixer.Sound(resource_path('audio/click.mp3')).play()
  canvas.coords(menuText1Stroke, (windowWidth / 2 + 2, 500 + 2))
  canvas.coords(menuText1, (windowWidth / 2, 500))
  canvas.coords(menuText2Stroke, (windowWidth / 2 + 2, 500 + 2))
  canvas.coords(menuText2, (windowWidth / 2, 500))
  canvas.coords(menuText3Stroke, (windowWidth / 2 + 2, 500 + 2))
  canvas.coords(menuText3, (windowWidth / 2, 500))
  canvas.coords(closeMenuBtn, (windowWidth / -20, 500))
  canvas.coords(menuBtn, (windowWidth - 20, 20))
  canvas.coords(purchaseLabelBackground, -10, -10, -10, -10)

def muteAudio(event):
  global songPlaying

  if songPlaying is True:
    songPlaying = False
  else:
    songPlaying = True

  if sfxPlaying is True:
    clickSound = pygame.mixer.Sound(resource_path('audio/click.mp3')).play()

def muteSfx(event):
  global  sfxPlaying

  if sfxPlaying is True:
    sfxPlaying = False
  else:
    sfxPlaying = True

  if sfxPlaying is True:
    clickSound = pygame.mixer.Sound(resource_path('audio/click.mp3')).play()

def playGame(event):
  canvas.coords(mainMenuBG, (windowWidth / 2 + 2, 500 + 2))
  canvas.coords(titleLabelStroke, (5000, 5000))
  canvas.coords(titleLabel, (5000, 5000))
  canvas.coords(startGameLabelStroke, (5000, 5000))
  canvas.coords(startGameLabel, (5000, 5000))
  canvas.coords(quitGameLabelStroke, (5000, 5000))
  canvas.coords(quitGameLabel, (5000, 5000))
  canvas.coords(titleBG, -10, -10, -10, -10)
  canvas.coords(cookieImageMainMenu, (5000, 5000))
  canvas.coords(cookieImage2MainMenu, (5000, 5000))
  if sfxPlaying is True:
    clickSound = pygame.mixer.Sound(resource_path('audio/click.mp3')).play()

pyglet.font.add_file(resource_path("fonts/font.ttf"))

app = tk.Tk()
pygame.init()

pygame.mixer.music.load(song)
pygame.mixer.music.play(-1)

canvas = Canvas(app, height=windowHeight, width=windowWidth, highlightthickness=0)
canvas.pack()

# Loaded images

bg_img = PhotoImage(file=resource_path("assets/bg.png"))
cookie = ImageTk.PhotoImage(Image.open(resource_path("assets/cookie.png")).resize((165, 165), Image.ANTIALIAS))
cookie2 = ImageTk.PhotoImage(Image.open(resource_path("assets/cookie.png")).resize((165, 165), Image.ANTIALIAS))
menuImage = ImageTk.PhotoImage(Image.open(resource_path("assets/menu.png")).resize((35, 35), Image.ANTIALIAS))
closeImage = ImageTk.PhotoImage(Image.open(resource_path("assets/close.png")).resize((35, 35), Image.ANTIALIAS))

# Main background

bg_label = canvas.create_image((windowWidth / -2, windowHeight / -2), image=bg_img, anchor=tk.N+tk.W)

# Cookie count background

cookieCountLabelBg = canvas.create_rectangle(windowHeight, 25, 0, windowWidth / 4, outline="", fill="black", width=2, stipple="gray50")

# Menu button

menuBtn = canvas.create_image(windowWidth + -20, 20, image=menuImage)
canvas.tag_bind(menuBtn, "<Button-1>", openMenu)

# Main cookie stuff

cookieCountLabelStroke = canvas.create_text((windowWidth / 2 + 2, 50 + 2), text=cookieCount, font=('Kavoon', 24), fill="black", justify=CENTER)
cookieCountLabel = canvas.create_text((windowWidth / 2, 50), text=cookieCount, font=('Kavoon', 24), fill="white", justify=CENTER)

cookieBtn = canvas.create_image(windowWidth / 2, windowHeight / 2 + 9, image=cookie2)
canvas.tag_bind(cookieBtn, "<Button-1>", addCookie)

# Purchase grandma

buyGrannyBtnStroke = canvas.create_text(windowWidth / 2 + 2, windowHeight / 2 + 110 + 2, text=f"Buy a Grandma ({grannyPrice})", font="Kavoon 14", fill="black", justify=CENTER)
buyGrannyBtn = canvas.create_text(windowWidth / 2, windowHeight / 2 + 110, text=f"Buy a Grandma ({grannyPrice})", font="Kavoon 14", fill="white", justify=CENTER)
canvas.tag_bind(buyGrannyBtn, "<Enter>", buyGrannyBtnHoverEnter)
canvas.tag_bind(buyGrannyBtn, "<Leave>", buyGrannyBtnHoverLeave)
canvas.tag_bind(buyGrannyBtn, "<Button-1>", buyGranny)

# upgradeLabelStroke = canvas.create_text((animatedLabelX + 1, animatedLabelY + 1), text="", font="Helvetica 18", fill="#ffffff")
# upgradeLabel = canvas.create_text((animatedLabelX, animatedLabelY), text="", font="Helvetica 18", fill="#0ec934")
# if upgrade != "plus1":
#   canvas.itemconfig(upgradeLabel, text=upgrade.replace("plus", "+"))

# Purchase label

purchaseLabelBackground = canvas.create_rectangle(-10, -10, -10, -10, fill='black', stipple="gray75")
purchaseLabelStroke = canvas.create_text((windowWidth / 2 + 2, windowHeight / 2 + 2), text="", font="Kavoon 20", fill="#000000", justify=CENTER)
purchaseLabel = canvas.create_text((windowWidth / 2, windowHeight / 2), text="", font="Kavoon 20", fill="#ffffff", justify=CENTER)

# Meu

menuText1Stroke = canvas.create_text((windowWidth / 2 + 2, 500 + 2), text="Audio", font="Kavoon 20", fill="#000000", justify=CENTER)
menuText1 = canvas.create_text((windowWidth / 2, 500), text="Audio", font="Kavoon 20", fill="#ffffff", justify=CENTER)
canvas.tag_bind(menuText1, "<Button-1>", muteAudio)

menuText2Stroke = canvas.create_text((windowWidth / 2 + 2, 500 + 2), text="SFX", font="Kavoon 20", fill="#000000", justify=CENTER)
menuText2 = canvas.create_text((windowWidth / 2, 500), text="SFX", font="Kavoon 20", fill="#ffffff", justify=CENTER)
canvas.tag_bind(menuText2, "<Button-1>", muteSfx)

menuText3Stroke = canvas.create_text((windowWidth / 2 + 2, 500 + 2), text="Quit Game", font="Kavoon 20", fill="#000000", justify=CENTER)
menuText3 = canvas.create_text((windowWidth / 2, 500), text="Quit Game", font="Kavoon 20", fill="#ffffff", justify=CENTER)
canvas.tag_bind(menuText3, "<Button-1>", quitApp)

closeMenuBtn = canvas.create_image(windowWidth + -20, 500, image=closeImage)
canvas.tag_bind(closeMenuBtn, "<Button-1>", closeMenu)

# Data saving label

saveDataLabelStroke = canvas.create_text((windowWidth / 2 + 2, windowHeight / 2 + 2), text="", font="Kavoon 20", fill="#000000", justify=CENTER)
saveDataLabel = canvas.create_text((windowWidth / 2, windowHeight / 2), text="", font="Kavoon 20", fill="#ffffff", justify=CENTER)

# Main Menu

mainMenuBG = canvas.create_image((windowWidth / -2, windowHeight / -2), image=bg_img, anchor=tk.N+tk.W)

titleBG = canvas.create_rectangle(windowHeight, 25, 0, windowWidth / 4, outline="", fill="black", width=2, stipple="gray50")
titleLabelStroke = canvas.create_text((windowWidth / 2 + 2, 50 + 2), text="Cookie Clicker", font=('Kavoon', 24), fill="black", justify=CENTER)
titleLabel = canvas.create_text((windowWidth / 2, 50), text="Cookie Clicker", font=('Kavoon', 24), fill="white", justify=CENTER)

startGameLabelStroke = canvas.create_text((windowWidth / 2 + 2, windowHeight / 2 - 25 + 2), text="Start Game", font=('Kavoon', 24), fill="black", justify=CENTER)
startGameLabel = canvas.create_text((windowWidth / 2, windowHeight / 2 - 25), text="Start Game", font=('Kavoon', 24), fill="white", justify=CENTER)
canvas.tag_bind(startGameLabel, "<Button-1>", playGame)

quitGameLabelStroke = canvas.create_text((windowWidth / 2 + 2, windowHeight / 2 + 25 + 2), text="Quit Game", font=('Kavoon', 24), fill="black", justify=CENTER)
quitGameLabel = canvas.create_text((windowWidth / 2, windowHeight / 2 + 25), text="Quit Game", font=('Kavoon', 24), fill="white", justify=CENTER)
canvas.tag_bind(quitGameLabel, "<Button-1>", quitApp)

cookieImageMainMenu = canvas.create_image((windowWidth - windowHeight + 25, windowHeight - 25), image=cookie)
cookieImage2MainMenu = canvas.create_image((windowWidth - 15, windowHeight + 15), image=cookie)

# Loops

app.after(grannySpeed, granny)
app.after(1, updateCookieCountLabel)
app.after(1, checkSong)

# App default shit

app.wm_title("Cookie Clicker")
app.geometry(f"{windowWidth}x{windowHeight}")
app.resizable(False, False)
app.iconbitmap(resource_path('cookie.ico'))
app.mainloop()
