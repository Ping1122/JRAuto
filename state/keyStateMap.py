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
from state.states.strategy import Strategy
from state.states.quitGame import QuitGame
from state.states.exerciseOpponentDetail import ExerciseOpponentDetail
from state.states.networkDisconnected import NetworkDisconnected
from state.states.obtainCombatResource import ObtainCombatResource 

keyStateMap = {
    StateKey.quitGame : QuitGame,
    StateKey.networkDisconnected : NetworkDisconnected,
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
    StateKey.strategy : Strategy,
    StateKey.exerciseOpponentDetail : ExerciseOpponentDetail,
    StateKey.obtainCombatResource : ObtainCombatResource,
    StateKey.unknown : Unknown,
}
