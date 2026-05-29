import logging


logger = logging.getLogger("schedule")


class ScheduleError(Exception):
    """ Base schedule exception """


class ScheduleValeError(ScheduleError):
    """ Base schedule value error """


class IntervalError(ScheduleError):
    """ An improper was used """
    

class Scheduler:
    def __init__(self):
        self.jobs = []


class Job:
    def __init__(self):
        pass
