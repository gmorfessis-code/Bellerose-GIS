#!/usr/bin/env python3
"""
Convert GeoJSON to qgis2web JavaScript format
Usage: python geojson_to_js.py input.geojson output.js variable_name
"""

import sys
import json

def convert_geojson_to_js(geojson_path, js_path, var_name):
    """Convert GeoJSON file to qgis2web JavaScript format"""
    
    # Read the GeoJSON file
    with open(geojson_path, 'r', encoding='utf-8') as f:
        geojson_data = json.load(f)
    
    # Write as JavaScript variable
    with open(js_path, 'w', encoding='utf-8') as f:
        f.write(f'var {var_name} = ')
        json.dump(geojson_data, f, ensure_ascii=False, indent=2)
        f.write(';')
    
    print(f"Successfully converted {geojson_path} to {js_path}")
    print(f"Variable name: {var_name}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python geojson_to_js.py input.geojson output.js variable_name")
        print("Example: python geojson_to_js.py parcels.geojson parcels.js json_parcels_2")
        sys.exit(1)
    
    geojson_file = sys.argv[1]
    js_file = sys.argv[2]
    variable_name = sys.argv[3]
    
    convert_geojson_to_js(geojson_file, js_file, variable_name)