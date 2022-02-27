from typing import List, Sequence, Tuple

class MyConvexHull:

	# Menerima seluruh data berupa posisi dari titik-titik
	def __init__(self, points):
		# Mengubah bentuk data ke generator of tuple 
		# sehingga dapat diolah
		param = ((i[0], i[1]) for i in points)
		res = self.make_hull(sorted(param))
		self.x_coords = [i[0] for i in res]
		self.x_coords.append(res[0][0])
		self.y_coords = [i[1] for i in res]
		self.y_coords.append(res[0][1])

	# Membuat Convex Hull
	def make_hull(self, points):
		# Menangani edgecase
		if len(points) <= 1:
			return list(points)

		# Membuat array untuk menampung hasil dari
		# pembagian area akibat algoritma divide and conquer	
		area_one = []
		area_two = []

		# Melakukan conquer sesuai dengan
		# pengertian dari convex hull
		for area in (area_one, area_two):
			if (area != area_one):
				points = reversed(points)

			for p in points:
				while len(area) >= 2:
					check1 = (area[-1][0] - area[-2][0]) * (p[1] - area[-2][1])
					check2 = (area[-1][1] - area[-2][1]) * (p[0] - area[-2][0])
					if (check1 >= check2):
						area.pop()
					else:
						break
				area.append(p)

			area.pop()
	
		if (len(area_one) == 1):
			if (area_one == area_two):
				area_two = []
		
		# Menggabungkan hasil dari kedua buah area
		area_one += area_two

		# Mengembalikan hasil
		return area_one