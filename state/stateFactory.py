from state.stateKey import StateKey
from state.states.unknown import Unknown
from state.states.attendence import Attendence
from state.states.chaseOrGiveUp import ChaseOrGiveUp
from state.states.combatPreparationQuickRepair import CombatPreparationQuickRepair
from state.states.combatPreparationQuickSupply import CombatPreparationQuickSupply
from state.states.combatPreparationStatistic import CombatPreparationStatistic
from state.states.enemyInfo import EnemyInfo
from state.states.forwardOrRetreat import ForwardOrRetreat
from state.states.gameClosed import GameClosed
from state.states.home import Home
from state.states.login import Login
from state.states.newsAndAnnouncement import NewsAndAnnouncement
from state.states.obtainLoginResource import ObtainLoginResource
from state.states.sailingOffCampaign import SailingOffCampaign
from state.states.sailingOffCombat import SailingOffCombat
from state.states.sailingOffExercise import SailingOffExercise
from state.states.sailingOffExpidition import SailingOffExpidition
from state.states.selectFormation import SelectFormation
from state.states.continueExpidition import ContinueExpidition
from state.states.newShip import NewShip
from state.states.flagShipSeriousDamaged import FlagShipSeriousDamaged
from state.states.battleResult import BattleResult
from state.states.slavagedShip import SlavagedShip
from state.states.expiditionResult import ExpiditionResult
from data.constants import IMG_RESOLUTION
from state.signals import Signals

class StateFactory:
	keyStateMap = {
		StateKey.attendence : Attendence,
		StateKey.chaseOrGiveUp : ChaseOrGiveUp,
		StateKey.combatPreparationQuickRepair : CombatPreparationQuickRepair,
		StateKey.combatPreparationQuickSupply : CombatPreparationQuickSupply,
		StateKey.combatPreparationStatistic : CombatPreparationStatistic,
		StateKey.enemyInfo : EnemyInfo,
		StateKey.forwardOrRetreat : ForwardOrRetreat,
		StateKey.gameClosed : GameClosed,
		StateKey.home : Home,
		StateKey.login : Login,
		StateKey.newsAndAnnouncement : NewsAndAnnouncement,
		StateKey.obtainLoginResource : ObtainLoginResource,
		StateKey.sailingOffCampaign : SailingOffCampaign,
		StateKey.sailingOffCombat : SailingOffCombat,
		StateKey.sailingOffExercise : SailingOffExercise,
		StateKey.sailingOffExpidition : SailingOffExpidition,
		StateKey.selectFormation : SelectFormation,
		StateKey.continueExpidition: ContinueExpidition,
		StateKey.flagShipSeriousDamaged : FlagShipSeriousDamaged,
		StateKey.newShip : NewShip,
		StateKey.battleResult : BattleResult,
		StateKey.slavagedShip : SlavagedShip,
		StateKey.expiditionResult : ExpiditionResult,
		StateKey.unknown : Unknown,
	}

	def __init__(self):
		pass

	def makeStateByScreenshot(self, screenshot):
		data = screenshot.getdata()
		stateClass = Unknown
		for state in self.keyStateMap.values():
			if all(
				self.debug(pos, data, color, state)
				#data[pos[1]*IMG_RESOLUTION[0]+pos[0]] == color
				for pos, color in state.signature.items()
			):
				stateClass = state
				break
		state = stateClass()
		self.setSignalByScreenshot(state, screenshot)
		return state

	def debug(self, pos, data, color, state):
		if state == ExpiditionResult:
			print(data[pos[1]*IMG_RESOLUTION[0]+pos[0]], color)
		return data[pos[1]*IMG_RESOLUTION[0]+pos[0]] in color

	def setSignalByScreenshot(self, state, screenshot):
		data = screenshot.getdata()
		for key, signature in state.sign.items():
			if all(
				self.debug(pos, data, color, key)
				#data[pos[1]*IMG_RESOLUTION[0]+pos[0]] == color
				for pos, color in signature.items()
			):
				state.signal[key] = True
			else:
				state.signal[key] = False
