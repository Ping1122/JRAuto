from state.state import State
from state.stateKey import StateKey
from state.transitions import Transitions

class SlavagedShip(State):
    signature = {
        (49, 1374) : ((31, 46, 75, 255), ),
        (105, 1133) : ((169, 171, 173, 255), ),
        (99, 1157) : ((34, 45, 55, 255), ),
        (98, 1294) : ((39, 41, 43, 255), ),
    }
    def __init__(self):
        super(SlavagedShip, self).__init__()
        self.key = StateKey.slavagedShip
        self.transition.update({
            Transitions.nextState : ({
                StateKey.newShip,
                StateKey.flagShipSeriousDamaged,
                StateKey.forwardOrRetreat,
                StateKey.sailingOffCombat,
            }, (2348, 1327, 10)),
        })
