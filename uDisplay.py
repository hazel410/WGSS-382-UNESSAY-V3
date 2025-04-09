import pygame
import uEnums

# ------------------------------------------------------------------ #
# This file handles all interactions with the screen-- i.e it displays
# shit. main will pass arguments to methods within and main may 
# acseess / modify variable directly
# ------------------------------------------------------------------ #

### ---misc---- ###
m_lineBigCode = "HCODE: LINE-TOO-BIG"
m_textBreakStart = "HCODE: STARTING-NOW"
### ----------- ###

colors = uEnums.COLORS()
dims = uEnums.DIMENSIONS()
fonts = uEnums.MISC()

class DAUBER:
  def __init__(self, screen):
    self.screen = screen
    self.cPlayArea = colors.playArea
    self.cScreenBorder = colors.screenBorder
    self.nBorderRect = [0, 0, dims.wScreen, dims.hBorder]
    self.eBorderRect = [dims.wScreen - dims.wBorder, 0, dims.wBorder, dims.hScreen - dims.hBorder]
    self.sBorderRect = [0, dims.hScreen - dims.hTextbox - (2 * dims.hBorder), dims.wScreen, dims.hTextbox + (2 * dims.hBorder)]
    self.wBorderRect = [0, 0, dims.wBorder, dims.hScreen]

  def drawPlayArea(self): 
    self.screen.fill(self.cPlayArea)

  def drawBorder(self):
    pygame.draw.rect(self.screen, self.cScreenBorder, self.nBorderRect)
    pygame.draw.rect(self.screen, self.cScreenBorder, self.eBorderRect)
    pygame.draw.rect(self.screen, self.cScreenBorder, self.sBorderRect)
    pygame.draw.rect(self.screen, self.cScreenBorder, self.wBorderRect)
  
  def drawEntity(self, rect, color):
    pygame.draw.rect(self.screen, color, rect)

class TEXTBOX:
  def __init__(self, screen, font=fonts.norm):
    self.screen = screen
    self.font = font
    self.vTextSpacer = dims.vTextSpacer
    self.cTextboxBorder = colors.textboxBorder
    self.cTextboxInner = colors.textboxInner
    self.cText = colors.text
    self.textboxBorderRect = [dims.wBorder,
                              dims.hScreen - dims.hBorder - dims.hTextbox,
                              dims.wScreen - (2 * dims.wBorder),
                              dims.hTextbox]
    self.textboxInnerRect = [dims.wBorder + dims.textboxBorder,
                             dims.hScreen - dims.hBorder - dims.hTextbox + dims.textboxBorder,
                             dims.wScreen - (2 * dims.wBorder) - (2 * dims.textboxBorder),
                             dims.hTextbox - (2* dims.textboxBorder)]
    self.textboxHorizontalSpace = dims.wScreen - (2 * dims.wBorder) - (2 * dims.textboxBorder) - (2 * dims.hTextSpacer)
    self.formatIndex = 0
    self.previousLine = m_textBreakStart
    self.currentLine = ""
    self.maxFontHeight = font.size("ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890.?!\"\'")[1]
    self.maxRows = (dims.hTextbox - self.vTextSpacer) // (self.maxFontHeight + self.vTextSpacer)
    self.drawXPos = dims.wBorder + dims.textboxBorder + dims.hTextSpacer
    self.drawYPos = dims.hScreen - dims.hBorder - dims.hTextbox + dims.textboxBorder + self.vTextSpacer
    # Null Assignments
    self.wordList = []
    self.numWords = -1
    self.formattedText = []
    self.displayTrue = False
  
  def applyText(self, rawText):
    # initializations
    self.formatIndex = 0
    self.previousLine = m_textBreakStart
    self.currentLine = ""
    self.wordList = rawText.split()
    self.numWords = len(self.wordList)
    outputTemp = []
    if rawText == "":
      self.displayTrue = False
    else:
      self.displayTrue = True

    # brute forces breaking text into multiple lines
    while self.numWords >= self.formatIndex + 1:

      # adds next word while avoiding leading space
      if self.previousLine == m_textBreakStart:
        self.currentLine = self.currentLine + self.wordList[self.formatIndex]
      else:
        self.currentLine = self.currentLine + " " + self.wordList[self.formatIndex]
      
      # checks if line is too big
      if self.font.size(self.currentLine)[0] > self.textboxHorizontalSpace:
        outputTemp.append(self.previousLine)
        self.previousLine = m_lineBigCode
        self.currentLine = self.wordList[self.formatIndex]
      else:
        self.previousLine = self.currentLine
        if self.formatIndex + 1 == self.numWords:
          outputTemp.append(self.previousLine)
      self.formatIndex += 1

      # handles an edge case
      if self.formatIndex == self.numWords and self.previousLine == m_lineBigCode:
        outputTemp.append(self.currentLine)
      # print("word number: " + str(self.formatIndex))
      # print("currentLine: " + str(self.currentLine))
      # print("previouLine: " + str(self.previousLine))
    self.formattedText = outputTemp

    # Pads final output with blank lines to be divisible by maxRows
    for x in range(self.maxRows - len(outputTemp) % self.maxRows):
      self.formattedText.append("")
  
  def advanceText(self):
    del self.formattedText[0:(self.maxRows)]
    if self.formattedText == []:
      self.displayTrue = False
  
  def drawTextbox(self):
    if len(self.formattedText) >= self.maxRows:
      pygame.draw.rect(self.screen, self.cTextboxBorder, self.textboxBorderRect)
      pygame.draw.rect(self.screen, self.cTextboxInner, self.textboxInnerRect)
      for x in range(self.maxRows):
        textRender = self.font.render(self.formattedText[x], True, self.cText)
        textRect = textRender.get_rect(topleft=[self.drawXPos, self.drawYPos + (x * (self.maxFontHeight + self.vTextSpacer))])
        self.screen.blit(textRender, textRect)