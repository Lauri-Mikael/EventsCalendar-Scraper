from getevents import get_events
from toexcelandcsv import toexcelandcsv

if __name__ == '__main__':
    results = get_events()
    toexcelandcsv(results)
