'''
// class WindowControlPanel() INHERITAGE PyQt5.QtWidgets  __  QWidget

// CLASS DEPENDENTS: 
	- AnimhoverButton() in /PROJECT/grafshell/Source/AnimhoverButton.py


// CONSTRUCTOR ARGUMENTS:
				NAMES:            VAR TYPES:     DEFAULT VARS:

	-   windowControlPanelHeight             int       30
	-    windowControlPanelColor   Optional [str]     None
	-   fawiconPathToDefaultIcon   Optional [str]     None
	-   fawiconPathToHoveredIcon   Optional [str]     None
	-    fawiconIconSizeScale              float      0.666
	-         programName                    str       ""
	-       additionalName                   str       ""
	-  minimizePathToDefaultIcon   Optional [str]     None
	-  minimizePathToHoveredIcon   Optional [str]     None
	-    minimizeIconSizeScale             float       0.4
	- fullscreenPathToDefaultIcon  Optional [str]     None
	- fullscreenPathToHoveredIcon  Optional [str]     None
	- lowscreenPathToDefaultIcon   Optional [str]     None
	- lowscreenPathToHoveredIcon   Optional [str]     None
	- checkoutscreenIconSizeScale          float       0.4
	- windowexitPathToDefaultIcon  Optional [str]     None
	- windowexitPathToHoveredIcon  Optional [str]     None
	-   windowexitIconSizeScale            float      0.466

	-       *args                  QWidget positional arguments
	-     **kwargs                 QWidget named arguments


// CLASS VARIABLES STORAGE:
	>> Public: 
		- controlPanel                   QHBoxLayout
		- cpFawiconButton            AnimhoverButton
		- cpProgramName                       QLabel
		- cpAdditionalName                    QLabel
		- cpMinimizeButton           AnimhoverButton
		- cpCheckoutscreenButton     AnimhoverButton
		- cpWindowexitButton         AnimhoverButton

	>> Private:
		- _windowControlPanelHeight              int
		- _windowControlPanelColor            QColor
		- _fawiconIconSizeScale                float
		- _minimizeIconSizeScale               float
		- _fullscreenPathToDefaultIcon  Optional[str]
		- _fullscreenPathToHoveredIcon  Optional[str]
		- _lowscreenPathToDefaultIcon   Optional[str]
		- _lowscreenPathToHoveredIcon   Optional[str]
		- _checkoutscreenIconSizeScale         float
		- _windowexitIconSizeScale             float

	>> Technical:
		- _oldMousePosition                   QPoint


// CLASS METHODS STORAGE:
	>> Public:
		- setFullscreenCSButtonIcons  _______( pathToDefaultIcon  Optional[str]  None;  pathToHoveredIcon  Optional[str]  None ) -> None
		- setLowscreenCSButtonIcons  ________( pathToDefaultIcon  Optional[str]  None;  pathToHoveredIcon  Optional[str]  None ) -> None
		- setFawiconIconSizeScale  __________( newScale                  float       ;                                         ) -> None
		- setMinimizeIconSizeScale  _________( newScale                  float       ;                                         ) -> None
		- setCheckoutscreenIconSizeScale  ___( newScale                  float       ;                                         ) -> None
		- setWindowexitIconSizeScale  _______( newScale                  float       ;                                         ) -> None
		- setWindowControlPanelColor  _______( color              Optional[str]      ;                                         ) -> None
		- setWindowControlPanelHeight  ______( newHeight                   int       ;                                         ) -> None
 
	>> Private:
		- _updateButtonSizes  _______________( newHeight                   int       ;  buttons                    List        ) -> None
		- _setUI  ___________________________(                                       ;                                         ) -> None
		- _switchCheckoutscreenButtonIcons  _(                                       ;                                         ) -> None
		- _setOldMousePosition  _____________( event                    QEvent       ;                                         ) -> None

	>> Technical:
		- mousePressEvent  __________________( event                    QEvent       ;                                         ) -> None
		- mouseReleaseEvent  ________________( event                    QEvent       ;                                         ) -> None
		- mouseMoveEvent  ___________________( event                    QEvent       ;                                         ) -> None
		- paintEvent  _______________________( event                    QEvent       ;                                         ) -> None
'''




#INDEPENDENCIES
from AnimhoverButton import AnimhoverButton

#LIBRARIES
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel
from PyQt5.QtCore import QEvent
from PyQt5.QtGui import QPainter
from typing import Optional, List




class WindowControlPanel(QWidget):
	def __init__(self,
				windowControlPanelHeight: int = 30,
				windowControlPanelColor: Optional[str] = None,
				
				fawiconPathToDefaultIcon: Optional[str] = None,
				fawiconPathToHoveredIcon: Optional[str] = None,
				fawiconIconSizeScale: float = 0.666,

				programName: str = "",
				additionalName: str = "",

				minimizePathToDefaultIcon: Optional[str] = None,
				minimizePathToHoveredIcon: Optional[str] = None,
				minimizeIconSizeScale: float = 0.4,

				fullscreenPathToDefaultIcon: Optional[str] = None,
				fullscreenPathToHoveredIcon: Optional[str] = None,
				lowscreenPathToDefaultIcon: Optional[str] = None,
				lowscreenPathToHoveredIcon: Optional[str] = None,
				checkoutscreenIconSizeScale: float = 0.4,

				windowexitPathToDefaultIcon: Optional[str] = None,
				windowexitPathToHoveredIcon: Optional[str] = None,
				windowexitIconSizeScale: float = 0.466,
				*args, **kwargs) -> None:
		super().__init__(*args, **kwargs)

		self._oldMousePosition: QPoint = self.pos()


		self.controlPanel = QHBoxLayout()
		self._windowControlPanelHeight: int = windowControlPanelHeight
		self.setWindowControlPanelColor(windowControlPanelColor)

		
		self.cpFawiconButton = AnimhoverButton(
			pathToDefaultIcon = fawiconPathToDefaultIcon,
			bgHoveranimEnabled = False
		)
		self.setFawiconIconSizeScale(fawiconIconSizeScale)

		
		self.cpProgramName = QLabel(programName+'  ')
		self.cpAdditionalName = QLabel(additionalName)


		self.cpMinimizeButton = AnimhoverButton(
			pathToDefaultIcon = minimizePathToDefaultIcon,
			pathToHoveredIcon = minimizePathToHoveredIcon,
			bgHoveredColor = 'rgb(42, 44, 44)'
		)
		self.setMinimizeIconSizeScale(minimizeIconSizeScale)

		self.setFullscreenCSButtonIcons(fullscreenPathToDefaultIcon, fullscreenPathToHoveredIcon)
		self.setLowscreenCSButtonIcons(lowscreenPathToDefaultIcon, lowscreenPathToHoveredIcon)
		self.cpCheckoutscreenButton = AnimhoverButton(
			pathToDefaultIcon = fullscreenPathToDefaultIcon,
			pathToHoveredIcon = fullscreenPathToHoveredIcon,
			bgHoveredColor = 'rgb(42, 44, 44)'
		)
		self.setCheckoutscreenIconSizeScale(checkoutscreenIconSizeScale)

		self.cpWindowexitButton = AnimhoverButton(
			pathToDefaultIcon = windowexitPathToDefaultIcon,
			pathToHoveredIcon = windowexitPathToHoveredIcon,
			bgHoveredColor = 'rgb(255, 0, 0)'
		)
		self.setWindowexitIconSizeScale(windowexitIconSizeScale)


		self.setWindowControlPanelHeight(windowControlPanelHeight)
		self._setUI()



	def setFullscreenCSButtonIcons(self, pathToDefaultIcon: Optional[str] = None, pathToHoveredIcon: Optional[str] = None) -> None:
		self._fullscreenPathToDefaultIcon: Optional[str] = pathToDefaultIcon
		self._fullscreenPathToHoveredIcon: Optional[str] = pathToHoveredIcon



	def setLowscreenCSButtonIcons(self, pathToDefaultIcon: Optional[str] = None, pathToHoveredIcon: Optional[str] = None) -> None:
		self._lowscreenPathToDefaultIcon: Optional[str] = pathToDefaultIcon
		self._lowscreenPathToHoveredIcon: Optional[str] = pathToHoveredIcon



	def setFawiconIconSizeScale(self, newScale: float) -> None:
		self._fawiconIconSizeScale: float = newScale

		newIconSize = int(self._windowControlPanelHeight*newScale)
		self.cpFawiconButton.setIconSize(newIconSize, newIconSize)



	def setMinimizeIconSizeScale(self, newScale: float) -> None:
		self._minimizeIconSizeScale: float = newScale

		newIconSize = int(self._windowControlPanelHeight*newScale)
		self.cpMinimizeButton.setIconSize(newIconSize, newIconSize)



	def setCheckoutscreenIconSizeScale(self, newScale: float) -> None:
		self._checkoutscreenIconSizeScale: float = newScale

		newIconSize = int(self._windowControlPanelHeight*newScale)
		self.cpCheckoutscreenButton.setIconSize(newIconSize, newIconSize)



	def setWindowexitIconSizeScale(self, newScale: float) -> None:
		self._windowexitIconSizeScale: float = newScale

		newIconSize = int(self._windowControlPanelHeight*newScale)
		self.cpWindowexitButton.setIconSize(newIconSize, newIconSize)



	def setWindowControlPanelColor(self, color: Optional[str]) -> None:
		self._windowControlPanelColor: QColor = self.cpFawiconButton._getColorWithValidation(color)
		self.update()



	def _updateButtonSizes(self, newHeight: int, buttons: List) -> None:
		newWidth = newHeight*2

			for button, scale in button_configs:
				scaledIconSize = int(newHeight*scale)

					button.setFixedSize(newWidth if button != self.cpFawiconButton else newHeight, newHeight)
					button.setIconSize(scaledIconSize, scaledIconSize)



	def setWindowControlPanelHeight(self, newHeight: int) -> None:
		self._windowControlPanelHeight = newHeight

		self.setFixedHeight(newHeight)

		self._updateButtonSizes(newHeight, [ (self.cpFawiconButton,        self._fawiconIconSizeScale       ),
													 (self.cpMinimizeButton,       self._minimizeIconSizeScale      ),
													 (self.cpCheckoutscreenButton, self._checkoutscreenIconSizeScale),
													 (self.cpWindowexitButton,     self._windowexitIconSizeScale    )  ] )



	def _setUI(self) -> None:
		self.controlPanel.setSpacing(0)
		self.controlPanel.setContentsMargins(0, 0, 0, 0)

		self.cpMinimizeButton.clicked.connect(parent().showMinimized)

		cpHorizontalDisplacement = QSpacerItem(40, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

		self.cpCheckoutscreenButton.clicked.connect(self._switchCheckoutscreenButtonIcons)
		self.cpCheckoutscreenButton.clicked.connect(parent().checkoutscreen)

		self.cpWindowexitButton.clicked.connect(parent().close)


		self.controlPanel.addWidget(self.cpFawiconButton)
		self.controlPanel.addWidget(self.cpProgramName)
		self.controlPanel.addWidget(self.cpAdditionalName)
		self.controlPanel.addItem(cpHorizontalDisplacement)
		self.controlPanel.addWidget(self.cpMinimizeButton)
		self.controlPanel.addWidget(self.cpCheckoutscreenButton)
		self.controlPanel.addWidget(self.cpWindowexitButton)


		parent().setWindowFlags(Qt.FramelessWindowHint)

		self.setLayout(self.controlPanel)
		self.setStyleSheet("background-color: transparent; font-size: 12px;")



	def _switchCheckoutscreenButtonIcons(self) -> None:
		if parent().isMaximized():
			self.cpCheckoutscreenButton.setDefaultIcon(self._fullscreenPathToDefaultIcon)
			self.cpCheckoutscreenButton.setHoveredIcon(self._fullscreenPathToHoveredIcon)
		else:
			self.cpCheckoutscreenButton.setDefaultIcon(self._lowscreenPathToDefaultIcon)
			self.cpCheckoutscreenButton.setHoveredIcon(self._lowscreenPathToHoveredIcon)



	def _setOldMousePosition(self, event: QEvent) -> None:
			if event.button() == Qt.LeftButton:
					self._oldMousePosition = event.globalPos()



	def mousePressEvent(self, event: QEvent) -> None:
		self._setOldMousePosition(event)



	def mouseReleaseEvent(self, event: QEvent) -> None:
		self._setOldMousePosition(event)

	

	def mouseMoveEvent(self, event: QEvent) -> None:
		if not parent().isFullScreen():
			if event.buttons() == Qt.LeftButton:
				delta = QPoint(event.globalPos() - self._oldMousePosition)

				parent().move(parent().x() + delta.x(), parent().y() + delta.y())
				
				self._oldMousePosition = event.globalPos()



	def paintEvent(self, event: QEvent) -> None:
		painter = QPainter(self)
		painter.setBrush(QBrush(self._windowControlPanelColor, Qt.SolidPattern))
		painter.setPen(Qt.NoPen)
		painter.drawRect(self.rect())