from task.tasks.combat31Resource import Combat31Resource
from task.tasks.combat55Boss import Combat55Boss
from task.tasks.combat61aAntiSS import Combat61aAntiSS
from task.tasks.combat61aSS import Combat61aSS
from task.tasks.combat71a import Combat71a
from task.tasks.combat74b import Combat74b
from task.tasks.combat81aAntiSS import Combat81aAntiSS
from task.tasks.combat81aCVL import Combat81aCVL
from task.tasks.combat82c import Combat82c
from task.tasks.combatStrategy import CombatStrategy
from task.tasks.exercise import Exercise
from task.tasks.campaign import Campaign
from task.taskKey import TaskKey

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
