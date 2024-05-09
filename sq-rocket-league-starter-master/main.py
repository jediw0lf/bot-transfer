# This file is for strategy

from util.objects import * 
from util.routines import *
from util.tools import find_hits

class Bot(GoslingAgent):
    # This function runs every in-game tick (every time the game updates anything)
    def run(self):
        self.print_debug()
        if self.get_intent() is not None:
            self.debug_intent()
            return
    debug_text = ''
    def print_debug(self):
        white = self.renderer.white()
        self.renderer.draw_string_2d(10, 150, 3, 3, self.debug_text, white)
            

        if self.kickoff_flag:
            self.set_intent(kickoff())
            return
        if self.me.boost > 99:
            self.set_intent(short_shot(self.foe_goal.location))
            return
        
        target_boost = self.get_closest_large_boost()
        if target_boost is not None:
            self.debug_text = 'getting boost'
            self.set_intent(goto(target_boost.location))
            return
        