#要么环要么一条链
class Song:
    def __init__(self, name):
        self.name = name
        self.next = None

    def next_song(self, song):
        self.next = song 
    
    def is_repeating_playlist(self):
        """
        :returns: (bool) True if the playlist is repeating, False if not.
        """
        curr = self
        playlist = set()
        while curr:
            if curr in playlist:
                return True
            playlist.add(curr)
            curr = curr.next
        return False
            
first = Song("Hello")
second = Song("Eye of the tiger")
    
first.next_song(second);
second.next_song(first);
    
print(first.is_repeating_playlist())
