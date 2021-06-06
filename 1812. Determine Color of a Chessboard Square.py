class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        if coordinates[0] in 'aceg' and int(coordinates[1]) % 2 == 0:
            return True
        if coordinates[0] in 'bdfh' and int(coordinates[1]) % 2 == 1:
            return True
        else:
            return False