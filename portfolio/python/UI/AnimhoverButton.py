#LIBRARIES
from typing import Optional
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QPropertyAnimation, QEvent, QSize
from PyQt5.QtGui import QPainter, QPaintEvent, QIcon, QPixmap, QColor





class AnimhoverButton(QPushButton):
	'''
	// class AnimhoverButton() INHERITAGE PyQt5.QtWidgets.QPushButton

	// OTHER DEPENDENCIES: 
		- no explicit inproject dependencies


	// CONSTRUCTOR ARGUMENTS:
				NAMES:      VAR TYPES:  DEFAULT VARS:

		-    buttonWidth         int         60
		-    buttonHeight        int         30
		-     iconWidth          int         12
		-     iconHeight         int         12
		- bgHoveranimEnabled    bool        True
		- bgHoveranimDuration    int         20
		-  pathToDefaultIcon     str         ''
		-  pathToHoveredIcon     str         ''
		-   bgDefaultColor       str         ''
		-   bgHoveredColor       str         ''

		-        *args          QPushButton positional arguments
		-     **kwargs         QPushButton named arguments


	// CLASS VARIABLES STORAGE:
		>> Public: 
			- no explicit public variables except for constructor arguments

		>> Private:
			- _bgHoveranim    QPropertyAnimation
			- _bgColor                    QColor
			- _bgDefaultColor             QColor
			- _bgHoveredColor             QColor
			- _defaultIcon                 QIcon
			- _hoveredIcon                 QIcon
			- _bgHoveranimEnabled           bool

		>> Technical:
			- _bgErrorColor               QColor
			- _bgTransparentColor         QColor
			- _errorIcon                   QIcon


	// CLASS METHODS STORAGE:
		>> Public:
			- setDefaultIcon  ____________( pathToImage      str  '' )
			- setHoveredIcon  ____________( pathToImage      str  '' )
			- setBGDefaultColor  _________( newColor         str  '' )
			- setBGHoveredColor  _________( newColor         str  '' )
			- setIsBGHoveranimEnable  ____( enableStatus    bool     )
			- setBGHoveranimDuration  ____( newDuration      int     )

		>> Private:
			- _getIconWithValidation  ____( pathToImage      str     ) -> QIcon
			- _getColorWithValidation  ___( newColor         str     ) -> QColor
			- _createErrorIcon  __________(                          ) -> QIcon

		>> Technical:
			- bgColor  __@property________(                          ) -> QColor
			- bgColor  __@bgColor.setter__( color         QColor     )

			- leaveEvent  ________________( a0   Optional      [QEvent]     )
			- enterEvent  ________________( a0   Optional      [QEvent]     )
			- paintEvent  ________________( a0   Optional [QPaintEvent]     )
	'''

	def __init__(self,
				buttonWidth: int = 60, buttonHeight: int = 30,
				iconWidth: int = 12, iconHeight: int = 12,
				bgHoveranimEnabled: bool = True,
				bgHoveranimDuration: int = 20,
				pathToDefaultIcon: str = '',
				pathToHoveredIcon: str = '',
				bgDefaultColor: str = '',
				bgHoveredColor: str = '',
				*args, **kwargs):
		super().__init__(*args, **kwargs)

		self._bgTransparentColor: QColor = QColor(255, 0, 255, 0)
		self._bgErrorColor:       QColor = QColor(255, 0, 255)
		self._errorIcon:           QIcon = self._createErrorIcon()

		self._bgHoveranim = QPropertyAnimation(self, b"bgColor")
		self.setIsBGHoveranimEnable(bgHoveranimEnabled)
		self.setBGHoveranimDuration(bgHoveranimDuration)

		self.setBGDefaultColor(bgDefaultColor)
		self.setBGHoveredColor(bgHoveredColor)
		self._bgColor = self._bgDefaultColor

		self.setDefaultIcon(pathToDefaultIcon)
		self.setHoveredIcon(pathToHoveredIcon)

		self.setIcon(self._defaultIcon)
		self.setIconSize(QSize(iconWidth, iconHeight))
		self.setFixedSize(buttonWidth, buttonHeight)
		self.setStyleSheet("background-color: transparent; border: none;")



	def _getIconWithValidation(self, pathToImage: str) -> QIcon:
		'''
		If in pathToImage:
			valid   path - return icon with your image;
			unvalid path - return icon with error image;
			empty   path - return empty icon; 
		'''
		createdIcon = QIcon(pathToImage) if pathToImage else QIcon()
		return createdIcon if not createdIcon.isNull() else self._errorIcon



	def setDefaultIcon(self, pathToImage: str = ''):
		self._defaultIcon = self._getIconWithValidation(pathToImage)



	def setHoveredIcon(self, pathToImage: str = ''):
		self._hoveredIcon = self._getIconWithValidation(pathToImage)



	def _getColorWithValidation(self, newColor: str) -> QColor:
		'''
		If in newColor:
			valid   color format - return your color;
			unvalid color format - return error color;
			empty   color format - return transparent color; 
		'''
		validColor = QColor(newColor) if newColor else self._bgTransparentColor
		return validColor if validColor.isValid() else self._bgErrorColor



	def setBGDefaultColor(self, newColor: str = ''):
		self._bgDefaultColor = self._getColorWithValidation(newColor)
		self._bgHoveranim.setStartValue(self._bgDefaultColor)



	def setBGHoveredColor(self, newColor: str = ''):
		self._bgHoveredColor = self._getColorWithValidation(newColor)
		self._bgHoveranim.setEndValue(self._bgHoveredColor)



	def setIsBGHoveranimEnable(self, enableStatus: bool):
		self._bgHoveranimEnabled = enableStatus



	def setBGHoveranimDuration(self, newDuration: int):
		'''
		newDuration:
			min > 0
			max < 10000
		'''
		self._bgHoveranim.setDuration(min(max(0, newDuration), 10000))		



	def leaveEvent(self, a0: Optional[QEvent]):
		if self._bgHoveranimEnabled:
			self._bgHoveranim.setDirection(QPropertyAnimation.Direction.Backward)
			self._bgHoveranim.start()

		else:
			self._bgColor = self._bgDefaultColor
			self.update()

		self.setIcon(self._defaultIcon)
		super().leaveEvent(a0)



	def enterEvent(self, a0: Optional[QEvent]):
		if self._bgHoveranimEnabled:
			self._bgHoveranim.setDirection(QPropertyAnimation.Direction.Forward)
			self._bgHoveranim.start()

		else:
			self._bgColor = self._bgHoveredColor
			self.update()

		self.setIcon(self._hoveredIcon)
		super().enterEvent(a0)



	def _createErrorIcon(self) -> QIcon:
		pixmap = QPixmap(2, 2)
		pixmap.fill(QColor(0, 0, 0))

		painter = QPainter(pixmap)
		painter.fillRect(0, 0, 1, 1, self._bgErrorColor)
		painter.fillRect(1, 1, 1, 1, self._bgErrorColor)
		painter.end()

		return QIcon(pixmap)



	@property
	def bgColor(self) -> QColor:
		return self._bgColor



	@bgColor.setter
	def bgColor(self, color: QColor):
		self._bgColor = color
		self.update()



	def paintEvent(self, a0: Optional[QPaintEvent]):
		painter: QPainter = QPainter(self)
		painter.fillRect(self.rect(), self._bgColor)

		super().paintEvent(a0)