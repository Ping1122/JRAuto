from tasks.combat31Resource import Combat31Resource
from tasks.combat55Boss import Combat55Boss
from tasks.combat61aAntiSS import Combat61aAntiSS
from tasks.combat61aSS import Combat61aSS
from tasks.combat71a import Combat71a
from tasks.combat74b import Combat74b
from tasks.combat81aAntiSS import Combat81aAntiSS
from tasks.combat81aCVL import Combat81aCVL
from tasks.combat82c import Combat82c
from tasks.combatStrategy import CombatStrategy
from tasks.exercise import Exercise
from tasks.campaign import Campaign
from taskKey import TaskKey

keyTaskMap = {
    TaskKey.combat31Resource : Combat31Resource,
    TaskKey.combat55Boss : Combat55Boss,
    TaskKey.combat61aAntiSS : Combat61aAntiSS,
    TaskKey.combat61aSS : Combat61aSS,
    TaskKey.combat71a : Combat71a,
    TaskKey.combat74b : Combat74b,
    TaskKey.combat81aAntiSS : Combat81aAntiSS,
    TaskKey.combat81aCVL : Combat81aCVL,
    TaskKey.combat82c : Combat82c,
    TaskKey.combatStrategy : CombatStrategy,
    TaskKey.exercise : Exercise,
    TaskKey.campaign : Campaign,
}
