"""Mission controller implementation for the submarine simulation."""


class PDController:
    """Discrete PD controller that retains the previous tracking error."""

    def __init__(self, kp: float = 0.15, kd: float = 0.6):
        self.kp = kp
        self.kd = kd
        self.previous_error = 0.0

    def reset(self) -> None:
        """Clear controller history before starting a new mission."""
        self.previous_error = 0.0

    def __call__(self, reference: float, observation: float) -> float:
        """Return a discrete PD action for the current reference and observation."""
        error = reference - observation
        action = self.kp * error + self.kd * (error - self.previous_error)
        self.previous_error = error
        return action


# Keep the convenient existing usage: ClosedLoop(plant, controller).
controller = PDController()
