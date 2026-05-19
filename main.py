import argparse
from shapely import wkt
from shapely.geometry import Point

def check_point_in_polygon(lon, lat, polygon_wkt):
    """
    Checks if a given longitude and latitude fall within a WKT polygon.
    """
    # Load the WKT string into a Shapely Polygon object
    polygon_obj = wkt.loads(polygon_wkt)
    
    # Create a Shapely Point (longitude is X, latitude is Y)
    point = Point(lon, lat)
    
    # Check if the polygon contains the point
    return polygon_obj.contains(point)

if __name__ == "__main__":
    # 1. Set up the argument parser to accept parameters from the command line
    parser = argparse.ArgumentParser(description="Check if a Longitude and Latitude are inside the defined polygon.")
    parser.add_argument("longitude", type=float, help="The longitude of the point to check")
    parser.add_argument("latitude", type=float, help="The latitude of the point to check")
    
    # 2. Parse the arguments provided by the user
    args = parser.parse_args()

    # 3. Define the polygon 
    polygon_wkt = """
    POLYGON ((-63.125925 46.191968, -63.129249 46.197682, -63.160804 46.209456, 
    -63.169438 46.206527, -63.178532 46.203442, -63.187627 46.200357, -63.196721 46.197272, 
    -63.205816 46.194188, -63.209914 46.192797, -63.210298 46.192726, -63.214264 46.192566, 
    -63.224337 46.19216, -63.234121 46.191766, -63.243753 46.187006, -63.244782 46.186932, 
    -63.252567 46.189465, -63.264739 46.190883, -63.276376 46.194511, -63.283669 46.198762, 
    -63.285552 46.209462, -63.286601 46.215494, -63.287049 46.221437, -63.28919 46.256974, 
    -63.286057 46.284623, -63.267947 46.316259, -63.262591 46.316431, -63.258916 46.315588, 
    -63.250191 46.313585, -63.250191 46.313585, -63.245568 46.312524, -63.201108 46.307234, 
    -63.200376 46.307313, -63.169357 46.310685, -63.138576 46.31403, -63.138447 46.314038, 
    -63.114907 46.314357, -63.114883 46.314358, -63.095651 46.314287, -63.09564 46.314287, 
    -63.092525 46.314249, -63.092522 46.314249, -63.068799 46.313913, -63.067935 46.313589, 
    -63.064911 46.311026, -63.061886 46.308496, -63.061877 46.308488, -63.057931 46.305128, 
    -63.000268 46.306833, -62.973955 46.317001, -62.949253 46.326546, -62.945115 46.32668, 
    -62.943625 46.326205, -62.938759 46.302137, -62.925934 46.279099, -62.917463 46.271131, 
    -62.865401 46.280221, -62.839903 46.284704, -62.823277 46.287894, -62.820549 46.287026, 
    -62.819639 46.285947, -62.818744 46.277951, -62.821265 46.270304, -62.821768 46.269359, 
    -62.824389 46.263356, -62.825523 46.257388, -62.828429 46.248574, -62.837435 46.225782, 
    -62.837467 46.225709, -62.842326 46.215242, -62.843221 46.210129, -62.842126 46.207027, 
    -62.842826 46.204904, -62.845563 46.201294, -62.864003 46.188252, -62.874333 46.175365, 
    -62.874335 46.175363, -62.886701 46.160015, -62.891081 46.149512, -62.891269 46.14859, 
    -62.893384 46.138214, -62.905311 46.122482, -62.922649 46.113706, -63.041611 46.121321, 
    -63.045423 46.122509, -63.117284 46.177317, -63.117637 46.177717, -63.125925 46.191968, 
    -63.125925 46.191968))
    """

    # 4. Run the check
    is_inside = check_point_in_polygon(args.longitude, args.latitude, polygon_wkt)

    # 5. Output the result
    if is_inside:
        print(f"\n[✓] The coordinate ({args.longitude}, {args.latitude}) is INSIDE the polygon.")
    else:
        print(f"\n[X] The coordinate ({args.longitude}, {args.latitude}) is OUTSIDE the polygon.")
