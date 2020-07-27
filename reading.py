class reading:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.time = time.time_ns()
        self.mag = np.sqrt(x**2 + y**2 + z**2)

def parse_data(input_data):
    decoded = input_data.decode()
    x = float(decoded.split('=')[1].split('\t')[0])/1000
    y = float(decoded.split('=')[2].split('\t')[0])/1000
    z = float(decoded.split('=')[3].split('\t')[0])/1000
    
    return reading(x,y,z)