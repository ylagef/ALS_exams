from parcial1_2014.exercise4.Line import Line


class Polygon:
    def __init__(self, points):
        self.points = points
        lines = []
        for i in range(len(points)):
            if i == len(points) - 1:
                lines.append(Line(points[i], points[0]))
            else:
                lines.append(Line(points[i], points[i + 1]))

        self.lines = lines

    def __str__(self):
        toret = "{"
        for l in self.lines:
            toret += str(l)
            if self.lines[-1] != l:
                toret += ", "
        toret += "}"
        return toret

    def getPoints(self):
        return self.points
