def make_readable(seconds):
    hours, remaining = divmod(seconds, 3600)
    minutes, seconds = divmod(remaining, 60)
    return "{0}:{1}:{2}".format(str(hours).zfill(2), str(minutes).zfill(2), str(seconds).zfill(2))