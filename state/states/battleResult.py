from state.state import State
from state.signals import Signals
from state.stateKey import StateKey
from state.transitions import Transitions

class BattleResult(State):
	signature = {
        (38, 39) : ((101, 112, 124, 255), ),
        (342, 133) : ((255, 255, 255, 255), ),
        (1139, 105) : ((255, 255, 255, 255), ),
        (376, 139) : ((255, 255, 255, 255), ),
	}
	def __init__(self):
		super().__init__()
		self.key = StateKey.battleResult
        self.sign.update({
            Signals.noDamagedShip: {
                (167, 373) : ((39, 174, 60, 255), ),
                (169, 575) : ((36, 173, 58, 255), ),
                (176, 775) : ((36, 173, 58, 255), ),
                (177, 974) : ((36, 173, 58, 255), (23, 45, 69, 255)),
                (175, 1173) : ((40, 175, 61, 255), (23, 45, 69, 255)),
                (175, 1376) : ((40, 175, 61, 255),(22, 44, 67, 255)),
            }
        })
		self.transition.update({
			Transitions.continue : ({
                StateKey.slavagedShip,
                StateKey.flagShipSeriousDamaged,
                StateKey.forwardOrRetreat,
                StateKey.sailingOffCombat,
                StateKey.sailingOffCampaign,
                StateKey.sailingOffExercise,
            }, (2348, 1327, 10)),
		})