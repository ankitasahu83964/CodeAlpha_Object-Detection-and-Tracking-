import numpy as np

class Sort:
    def __init__(self):
        self.objects = {}
        self.id_count = 0

    def update(self, detections):
        new_objects = {}

        for det in detections:
            x1, y1, x2, y2, _ = det
            cx = int((x1 + x2) / 2)
            cy = int((y1 + y2) / 2)

            matched_id = None

            for obj_id, (px, py) in self.objects.items():
                dist = np.sqrt((cx - px)**2 + (cy - py)**2)

                if dist < 300:
                    matched_id = obj_id
                    break

            if matched_id is None:
                self.id_count += 1
                matched_id = self.id_count

            new_objects[matched_id] = (cx, cy)

        self.objects = new_objects

        result = []
        for obj_id, (cx, cy) in self.objects.items():
            result.append([cx-20, cy-20, cx+20, cy+20, obj_id])

        return result