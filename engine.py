class Engine:
    def __init__(self, kill_method):
        self.kill = kill_method

    def shutdown(self, signum, frame):
        """Order shutdown this object."""
        self.kill()

    def run(self):
        """Execute the grab and print."""
        pass
