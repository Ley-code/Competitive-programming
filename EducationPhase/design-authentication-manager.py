class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.timeToLive = timeToLive        
        self.hashmap = {}    
    def generate(self, tokenId: str, currentTime: int) -> None:
        self.hashmap[tokenId] = currentTime
    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.hashmap:
            if (currentTime - self.hashmap[tokenId]) < self.timeToLive:
                self.hashmap[tokenId] = currentTime
            else:
                del self.hashmap[tokenId]
    def countUnexpiredTokens(self, currentTime: int) -> int:
        count = 0
        for value in self.hashmap.values():
            if (value+self.timeToLive)>currentTime:
                count+=1
        return count


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)