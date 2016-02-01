from decimal import Decimal, getcontext
from vector import *
from line import *
from plane import *
from linsys import *

getcontext().prec = 30

# vector1 = Vector([8.218,-9.341])
# vector2 = Vector([7.119,8.215])
# vector3 = Vector([1.671,-1.012,-0.318])
# print vector1.plus(Vector([-1.129,2.111]))
# print vector2.minus(Vector([-8.223,0.878]))
# print vector3.times_scalar(7.41)

# vector4 = Vector([-0.221,7.437])
# vector5 = Vector([8.813,-1.331,-6.247])
# vector6 = Vector([5.581,-2.136])
# vector7 = Vector([1.996,3.108,-4.554])
# print vector4.magnitude()
# print vector5.magnitude()
# print vector6.unit_vector()
# print vector7.unit_vector()

# vector8 = Vector([7.887,4.138])
# vector9 = Vector([-5.955,-4.904,-1.874])
# print vector8.dot_product(Vector([-8.802,6.776]))
# print vector9.dot_product(Vector([-4.496,-8.755,7.103]))

# vector10 = Vector([3.183,-7.627])
# vector11 = Vector([7.35,0.221,5.188])
# print vector10.angle_between_vectors(Vector([-2.668,5.319]))
# print vector11.angle_between_vectors(Vector([2.751,8.259,3.985]), False)

# vector1A = Vector([-7.579,-7.88])
# vector2A = Vector([22.737,23.64])
# vector1B = Vector([-2.029,9.97,4.172])
# vector2B = Vector([-9.231,-6.639,-7.245])
# vector1C = Vector([-2.328,-7.284,-1.214])
# vector2C = Vector([-1.821,1.072,-2.94])
# vector1D = Vector([2.118,4.827])
# vector2D = Vector([0,0])
# print "Vectors A:"
# print vector1A.is_parallel(vector2A)
# print vector1A.is_orthogonal(vector2A)
# print "Vectors B:"
# print vector1B.is_parallel(vector2B)
# print vector1B.is_orthogonal(vector2B)
# print "Vectors C:"
# print vector1C.is_parallel(vector2C)
# print vector1C.is_orthogonal(vector2C)
# print "Vectors D:"
# print vector1D.is_parallel(vector2D)
# print vector1D.is_orthogonal(vector2D)

# vectorV1 = Vector([3.039,1.879])
# vectorB1 = Vector([0.825,2.036])
# vectorV2 = Vector([-9.88,-3.264,-8.159])
# vectorB2 = Vector([-2.155,-9.353,-9.473])
# vectorV3 = Vector([3.009,-6.172,3.692,-2.51])
# vectorB3 = Vector([6.404,-9.144,2.759,8.718])

# print vectorV1.get_parallel_projection(vectorB1)
# print vectorV2.get_orthogonal_projection(vectorB2)
# print vectorV3.get_parallel_projection(vectorB3)
# print vectorV3.get_orthogonal_projection(vectorB3)

# vectorV1 = Vector([8.462,7.893,-8.187])
# vectorW1 = Vector([6.984,-5.975,4.778])
# vectorV2 = Vector([-8.987,-9.838,5.031])
# vectorW2 = Vector([-4.268,-1.861,-8.866])
# vectorV3 = Vector([1.5,9.547,3.691])
# vectorW3 = Vector([-6.007,0.124,5.772])

# print vectorV1.cross_product(vectorW1)
# print vectorV2.area_of_parallelogram_spanned(vectorW2)
# print vectorV3.area_of_triangle_spanned(vectorW3)

# lineA1 = Line([Decimal(4.046),Decimal(2.836)], 1.21)
# lineA2 = Line([Decimal(10.115),Decimal(7.09)], 3.025)

# lineB1 = Line([Decimal(7.204),Decimal(3.182)], 8.68)
# lineB2 = Line([Decimal(8.172),Decimal(4.114)], 9.883)

# lineC1 = Line([Decimal(1.182),Decimal(5.562)], 6.744)
# lineC2 = Line([Decimal(1.773),Decimal(8.343)], 9.525)

# print "A Line"
# same_line = lineA1.__eq__(lineA2)
# print "Are the same line?: %s" % same_line
# if(not same_line):
# 	parallel = lineA1.is_parallel(lineA2)
# 	print "Are Parallel?: %s" % parallel
# 	if(not parallel):
# 		print "Intersection: %s" % lineA1.intersection(lineA2)

# print "B Line"
# same_line = lineB1.__eq__(lineB2)
# print "Are the same line?: %s" % same_line
# if(not same_line):
# 	parallel = lineB1.is_parallel(lineB2)
# 	print "Are Parallel?: %s" % parallel
# 	if(not parallel):
# 		print "Intersection: %s" % lineB1.intersection(lineB2)

# print "C Line"
# same_line = lineC1.__eq__(lineC2)
# print "Are the same line?: %s" % same_line
# if(not same_line):
# 	parallel = lineC1.is_parallel(lineC2)
# 	print "Are Parallel?: %s" % parallel
# 	if(not parallel):
# 		print "Intersection: %s" % lineC1.intersection(lineC2)


# planeA1 = Plane([Decimal(4.046),Decimal(2.836)], 1.21)
# planeA2 = Plane([Decimal(10.115),Decimal(7.09)], 3.025)

# planeB1 = Plane([Decimal(7.204),Decimal(3.182)], 8.68)
# planeB2 = Plane([Decimal(8.172),Decimal(4.114)], 9.883)

# planeC1 = Plane([Decimal(1.182),Decimal(5.562)], 6.744)
# planeC2 = Plane([Decimal(1.773),Decimal(8.343)], 9.525)

# print "A Plane"
# same_plane = planeA1.__eq__(planeA2)
# print "Are the same plane?: %s" % same_plane
# if(not same_plane):
# 	parallel = planeA1.is_parallel(planeA2)
# 	print "Are Parallel?: %s" % parallel

# print "B Plane"
# same_plane = planeB1.__eq__(planeB2)
# print "Are the same plane?: %s" % same_plane
# if(not same_plane):
# 	parallel = planeB1.is_parallel(planeB2)
# 	print "Are Parallel?: %s" % parallel

# print "C Plane"
# same_plane = planeC1.__eq__(planeC2)
# print "Are the same plane?: %s" % same_plane
# if(not same_plane):
# 	parallel = planeC1.is_parallel(planeC2)
# 	print "Are Parallel?: %s" % parallel

# p0 = Plane(['1','1','1'], constant_term='1')
# p1 = Plane(['0','1','0'], constant_term='2')
# p2 = Plane(['1','1','-1'], constant_term='3')
# p3 = Plane(['1','0','-2'], constant_term='2')

# s = LinearSystem([p0,p1,p2,p3])

# print s.indices_of_first_nonzero_terms_in_each_row()
# print '{},{},{},{}'.format(s[0],s[1],s[2],s[3])
# print len(s)
# print s

# s[0] = p1
# print s

# print MyDecimal('1e-9').is_near_zero()
# print MyDecimal('1e-11').is_near_zero()

# Linear System Test 2

p1 = Plane(normal_vector=['1','1','1'], constant_term='1')
p2 = Plane(normal_vector=['0','1','1'], constant_term='2')
s = LinearSystem([p1,p2])
t = s.compute_triangular_form()
if not (t[0] == p1 and
        t[1] == p2):
    print 'test case 1 failed'

# p1 = Plane(normal_vector=['1','1','1'], constant_term='1')
# p2 = Plane(normal_vector=['1','1','1'], constant_term='2')
# s = LinearSystem([p1,p2])
# t = s.compute_triangular_form()
# if not (t[0] == p1 and t[1] == Plane(constant_term='1')):
#     print 'test case 2 failed'

# p1 = Plane(normal_vector=['1','1','1'], constant_term='1')
# p2 = Plane(normal_vector=['0','1','0'], constant_term='2')
# p3 = Plane(normal_vector=['1','1','-1'], constant_term='3')
# p4 = Plane(normal_vector=['1','0','-2'], constant_term='2')
# s = LinearSystem([p1,p2,p3,p4])
# t = s.compute_triangular_form()
# if not (t[0] == p1 and
#         t[1] == p2 and
#         t[2] == Plane(normal_vector=['0','0','-2'], constant_term='2') and
#         t[3] == Plane()):
#     print 'test case 3 failed'

p1 = Plane(normal_vector=['0','1','1'], constant_term='1')
p2 = Plane(normal_vector=['1','-1','1'], constant_term='2')
p3 = Plane(normal_vector=['1','2','-5'], constant_term='3')
s = LinearSystem([p1,p2,p3])
t = s.compute_triangular_form()
if not (t[0] == Plane(normal_vector=['1','-1','1'], constant_term='2') and
        t[1] == Plane(normal_vector=['0','1','1'], constant_term='1') and
        t[2] == Plane(normal_vector=['0','0','-9'], constant_term='-2')):
    print 'test case 4 failed'
