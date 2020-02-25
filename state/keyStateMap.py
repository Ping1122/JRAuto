from stateKey import StateKey
from states.unknown import Unknown
from states.attendence import Attendence
from states.chaseOrGiveUp import ChaseOrGiveUp
from states.combatPreparationQuickRepair import CombatPreparationQuickRepair
from states.combatPreparationQuickSupply import CombatPreparationQuickSupply
from states.combatPreparationStatistic import CombatPreparationStatistic
from states.enemyInfo import EnemyInfo
from states.forwardOrRetreat import ForwardOrRetreat
from states.gameClosed import GameClosed
from states.home import Home
from states.login import Login
from states.newsAndAnnouncement import NewsAndAnnouncement
from states.obtainLoginResource import ObtainLoginResource
from states.sailingOffCampaign import SailingOffCampaign
from states.sailingOffCombat import SailingOffCombat
from states.sailingOffExercise import SailingOffExercise
from states.sailingOffExpidition import SailingOffExpidition
from states.selectFormation import SelectFormation
from states.continueExpidition import ContinueExpidition
from states.newShip import NewShip
from states.flagShipSeriousDamaged import FlagShipSeriousDamaged
from states.battleResult import BattleResult
from states.slavagedShip import SlavagedShip
from states.expiditionResult import ExpiditionResult
from states.strategy import Strategy
from states.quitGame import QuitGame
from states.exerciseOpponentDetail import ExerciseOpponentDetail
from states.networkDisconnected import NetworkDisconnected
from states.obtainCombatResource import ObtainCombatResource 

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
