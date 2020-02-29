from state.state import State
from state.stateKey import StateKey
from state.transitions import Transitions

class SlavagedShip(State):
    signature = {
        (28, 428) : ((173, 170, 173), ),
        (27, 460) : ((173, 174, 173), ),
        (33, 464) : ((214, 215, 214), ),
        (29, 472) : ((41, 40, 41), ),
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
            }, (649, 459, 3)),
        })
