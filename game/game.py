import pygame
from game.settings import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    FPS,
    GAME_TITLE
)

# Game State Constants
OPERATIONAL_MAP = 'OPERATIONAL_MAP'  # Campaign map layer
TACTICAL_MAP = 'TACTICAL_MAP'        # Real-time tactical battle layer
PAUSED = 'PAUSED'

class OperationalManager:
    def update(self, dt):
        # Future systems:
        # - AI commanders strategic movement
        # - Army movement on world map
        # - Campaign economy & logistics
        pass

    def render(self, screen):
        # Draw the strategic campaign map
        screen.fill((40, 60, 100))  # Temporary distinct color for Operational Map (e.g., blueish)

class TacticalManager:
    def update(self, dt):
        # Future systems:
        # - Unit movement & pathfinding
        # - Real-time combat & flanking
        # - Morale calculations & routing
        pass

    def render(self, screen):
        # Draw the tactical battle map
        screen.fill((40, 100, 40))  # Your original green background for battles

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption(GAME_TITLE)
        self.clock = pygame.time.Clock()
        self.running = True

        # Game State & Managers
        self.current_state = OPERATIONAL_MAP  # Start on the campaign map
        self.operational_manager = OperationalManager()
        self.tactical_manager = TacticalManager()

        # Timing parameters for Fixed Timestep logic updates
        self.time_step = 1.0 / FPS  # Constant step size for logic updates (e.g., 1/60s)
        self.accumulated_time = 0.0

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            
            # Future system: Handle state-specific inputs here
            # e.g., Pass event to self.operational_manager.handle_input(event)

    def update(self, dt):
        # Delegate updates based on the active game state
        if self.current_state == OPERATIONAL_MAP:
            self.operational_manager.update(dt)
        elif self.current_state == TACTICAL_MAP:
            self.tactical_manager.update(dt)
        elif self.current_state == PAUSED:
            pass

    def draw(self):
        # Delegate rendering based on the active game state
        if self.current_state == OPERATIONAL_MAP:
            self.operational_manager.render(self.screen)
        elif self.current_state == TACTICAL_MAP:
            self.tactical_manager.render(self.screen)

        pygame.display.flip()

    def change_state(self, new_state, battle_data=None):
        print(f"Changing game state to: {new_state}")
        self.current_state = new_state
        
        if new_state == TACTICAL_MAP:
            self.init_tactical_battle(battle_data)

    def init_tactical_battle(self, battle_data):
        # Load the tactical map based on encounter data from the operational map
        pass

    def run(self):
        while self.running:
            # clock.tick(FPS) returns time passed since last frame in milliseconds
            # Convert to seconds for delta_time consistency
            delta_time = self.clock.tick(FPS) / 1000.0

            # Prevent "spiral of death" during heavy lag spikes (max 0.25 seconds)
            if delta_time > 0.25:
                delta_time = 0.25

            self.accumulated_time += delta_time

            # 1. Handle user inputs
            self.handle_events()

            # 2. FIXED UPDATE: Process game logic to catch up with real time
            while self.accumulated_time >= self.time_step:
                self.update(self.time_step)
                self.accumulated_time -= self.time_step

            # 3. RENDER: Draw the graphics
            self.draw()

        pygame.quit()

# Run the game
if __name__ == "__main__":
    my_rts = Game()
    my_rts.run()
