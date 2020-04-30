from typing import Optional, Union, Tuple, List, overload
class VectorElementwiseProxy: ...

def enable_swizzling() -> None: ...
def disable_swizzling() -> None: ...

class Vector2:
    x: float
    y: float
    def __init__(self, x: Optional[Union[float, Vector2, Tuple[float, float], List[float]]]=0, y: Optional[float]=0) -> None: ...
    def dot(self, other: Vector2) -> float: ...
    def cross(self, other: Vector2) -> Vector2: ...
    def magnitude(self) -> float: ...
    def magnitude_squared(self) -> float: ...
    def length(self) -> float: ...
    def length_squared(self) -> float: ...
    def normalize(self) -> Vector2: ...
    def normalize_ip(self) -> None: ...
    def is_normalized(self) -> bool: ...
    def scale_to_length(self, value: float) -> None: ...
    def reflect(self, other: Vector2) -> Vector2: ...
    def reflect_ip(self, other: Vector2) -> None: ...
    def distance_to(self, other: Vector2) -> float: ...
    def distance_squared_to(self, other: Vector2) -> float: ...
    def lerp(self, other: Vector2, value: float) -> Vector2: ...
    def slerp(self, other: Vector2, value: float) -> Vector2: ...
    def elementwise(self) -> VectorElementwiseProxy: ...
    def rotate(self, angle: float) -> Vector2: ...
    def rotate_rad(self, angle: float) -> Vector2: ...
    def rotate_ip(self, angle: float) -> None: ...
    def rotate_ip_rad(self, angle: float) -> None: ...
    def angle_to(self, other: Vector2) -> float: ...
    def as_polar(self) -> Tuple[float, float]: ...
    def from_polar(self, polar_value: Union[List[float], Tuple[float, float]]) -> None: ...
    def update(self, first: Optional[Union[float, Vector2, Tuple[float, float], List[float]]]=0, second: Optional[float]=0) -> None: ...

class Vector3:
    x: float
    y: float
    z: float
    @overload
    def __init__(self, xyz: Optional[Union[float, Tuple[float, float, float], List[float], Vector3]]=0) -> None: ...
    @overload
    def __init__(self, x: int, y: int, z) -> None: ...
    def dot(self, other: Vector3) -> float: ...
    def cross(self, other: Vector3) -> Vector3: ...
    def magnitude(self) -> float: ...
    def magnitude_squared(self) -> float: ...
    def length(self) -> float: ...
    def length_squared(self) -> float: ...
    def normalize(self) -> Vector3: ...
    def normalize_ip(self) -> None: ...
    def is_normalized(self) -> bool: ...
    def scale_to_length(self, value: float) -> None: ...
    def reflect(self, other: Vector3) -> Vector3: ...
    def reflect_ip(self, other: Vector3) -> None: ...
    def distance_to(self, other: Vector3) -> float: ...
    def distance_squared_to(self, other: Vector3) -> float: ...
    def lerp(self, other: Vector3, value: float) -> Vector3: ...
    def slerp(self, other: Vector3, value: float) -> Vector3: ...
    def elementwise(self) -> VectorElementwiseProxy: ...
    def rotate(self, angle: float, axis: Vector3) -> Vector3: ...
    def rotate_rad(self, angle: float, axis: Vector3) -> Vector3: ...
    def rotate_ip(self, angle: float, axis: Vector3) -> None: ...
    def rotate_ip_rad(self, angle: float, axis: Vector3) -> None: ...
    def rotate_x(self, angle: float) -> Vector3: ...
    def rotate_x_rad(self, angle: float) -> Vector3: ...
    def rotate_x_ip(self, angle: float) -> None: ...
    def rotate_x_ip_rad(self, angle: float) -> None: ...
    def rotate_y(self, angle: float) -> Vector3: ...
    def rotate_y_rad(self, angle: float) -> Vector3: ...
    def rotate_y_ip(self, angle: float) -> None: ...
    def rotate_y_ip_rad(self, angle: float) -> None: ...
    def rotate_z(self, angle: float) -> Vector3: ...
    def rotate_z_rad(self, angle: float) -> Vector3: ...
    def rotate_z_ip(self, angle: float) -> None: ...
    def rotate_z_ip_rad(self, angle: float) -> None: ...
    def angle_to(self, other: Vector3) -> float: ...
    def as_spherical(self) -> Tuple[float, float, float]: ...
    def from_spherical(self, spherical: Tuple[float, float, float]) -> None: ...
    @overload
    def update(self, xyz: Optional[Union[float, Tuple[float, float, float], List[float], Vector3]]=0) -> None: ...
    @overload
    def update(self, x: int, y: int, z) -> None: ...
