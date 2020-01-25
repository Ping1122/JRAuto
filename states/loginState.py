from states.state import State
from states.homeState import HomeState
from states.newsAndAnnouncementState import NewsAndAnnouncementState

class LoginState(State):
	signature = {
		(72, 704) : (56, 56, 56, 255),
		(144, 701) : (187, 187, 187, 255),
		(40, 695) : (183, 197, 201, 255),
		(134, 683) : (237, 237, 237, 255),
		(102, 730) : (237, 237, 237, 255),
		(180, 727) : (237, 237, 237, 255),
	}

	def __init__(self):
		super().__init__()
		self.transition = {
			(1323, 724, 5) : {HomeState, newsAndAnnouncementState}
		}