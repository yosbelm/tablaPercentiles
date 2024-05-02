import pandas as pd

tabla_peso_edad_boys = pd.DataFrame([
    [2.8, 3.2,  3.6,  4.1,  4.9,  5.6, 6.6],
    [3.5, 4.1,  4.5,  5.2,  5.9,  6.6, 7.7],
    [4.2, 4.8,  5.3,  6.0,  6.7,  7.4, 8.5],
    [4.8, 5.4,  6.0,  6.6,  7.4,  8.2, 9.2],
    [5.3, 6.0,  6.6,  7.2,  8.0,  8.8, 9.8],
    [5.7, 6.4,  7.1,  7.7,  8.5,  9.2, 10.3],
    [6.1, 6.8,  7.5,  8.2,  8.9,  9.9, 10.8],
    [6.4, 7.1,  7.8,  8.6,  9.3,  10.2, 11.2],
    [6.7, 7.4,  8.1,  8.9,  9.7,  10.5, 11.6],
    [7.0, 7.7,  8.4,  9.2,  10.0, 10.8, 11.9],
    [7.3, 8.0,  8.7,  9.5,  10.3, 11.1, 12.2],
    [7.6, 8.3,  9.0,  9.8,  10.5, 11.3, 12.5],
    [7.9, 8.5,  9.2,  10.0, 10.7, 11.5, 12.8],
    [8.1, 8.7,  9.5,  10.2, 10.9, 11.7, 13.0],
    [8.3, 8.9,  9.7,  10.4, 11.1, 12.0, 13.2],
    [8.5, 9.1,  9.9,  10.6, 11.3, 12.2, 13.4],
    [8.7, 9.3,  10.1, 10.8, 11.6, 12.5, 13.6],
    [8.8, 9.4,  10.2, 11.0, 11.8, 12.7, 13.8],
    [8.9, 9.6,  10.4, 11.1, 12.0, 12.9, 14.0],
    [9.0, 9.7,  10.5, 11.3, 12.2, 13.1, 14.2],
    [9.1, 9.8,  10.7, 11.4, 12.4, 13.3, 14.4],
    [9.2, 9.9,  10.8, 11.6, 12.6, 13.5, 14.6],
    [9.3, 10.0, 10.9, 11.8, 12.7, 13.7, 14.8],
    [9.4, 10.1, 11.1, 11.9, 12.9, 13.9, 15.0]], columns=[3, 10, 25, 50, 75, 90, 97])
        
tabla_peso_edad_girls = pd.DataFrame([ 
    [2.8, 3.2, 3.6, 4.1, 4.7, 5.2, 6.1],
    [3.4, 3.9, 4.3, 4.9, 5.4, 6.0, 6.9],
    [3.9, 4.5, 5.0, 5.7, 6.2, 6.7, 7.6],
    [4.4, 5.0, 5.6, 6.3, 6.8, 7.4, 8.3],
    [4.8, 5.5, 6.1, 6.8, 7.4, 8.1, 9.0],
    [5.2, 5.9, 6.5, 7.3, 7.9, 8.7, 9.7],
    [5.6, 6.3, 6.9, 7.7, 8.4, 9.2, 10.2],
    [5.9, 6.7, 7.4, 8.0, 8.8, 9.6, 10.6],
    [6.2, 7.0, 7.7, 8.3, 9.1, 9.9, 11.0],
    [6.5, 7.3, 7.9, 8.6, 9.4, 10.2, 11.4],
    [6.7, 7.5, 8.1, 8.8, 9.7, 10.5, 11.7],
    [7.0, 7.7, 8.3, 9.0, 9.9, 10.8, 11.9],
    [7.2, 7.9, 8.5, 9.3, 10.1, 11.1, 12.1],
    [7.4, 8.1, 8.7, 9.5, 10.3, 11.3, 12.3],
    [7.7, 8.4, 9.0, 9.7, 10.6, 11.5, 12.5],
    [7.9, 8.6, 9.2, 9.9, 10.8, 11.7, 12.7],
    [8.1, 8.8, 9.4, 10.1, 11.0, 11.9, 12.9],
    [8.2, 9.0, 9.6, 10.3, 11.2, 12.1, 13.1],
    [8.3, 9.2, 9.8, 10.5, 11.4, 12.3, 13.4],
    [8.4, 9.3, 9.9, 10.7, 11.6, 12.5, 13.6],
    [8.5, 9.4, 10.0, 10.9, 11.8, 12.7, 13.9],
    [8.6, 9.5, 10.1, 11.1, 12.0, 12.9, 14.1],
    [8.7, 9.6, 10.3, 11.2, 12.2, 13.1, 14.3],
    [8.8, 9.7, 10.4, 11.3, 12.3, 13.3, 14.5]], columns = [3, 10, 25, 50, 75, 90, 97])


tabla_talla_edad_boys = pd.DataFrame([
    [48.2, 49.8, 51.5, 53.3, 55.1, 56.8, 58.4],
    [52.1, 53.8, 55.4, 57.3, 59.2, 60.8, 62.5],
    [54.7, 56.4, 58.1, 60.0, 61.9, 63.6, 65.3],
    [57.0, 58.7, 60.5, 62.4, 64.3, 66.1, 67.8],
    [59.2, 60.9, 62.7, 64.6, 66.5, 68.3, 70.0],
    [67.0, 62.7, 64.5, 66.5, 68.5, 70.3, 72.0],
    [62.5, 64.3, 66.1, 68.1, 70.1, 71.9, 73.7],
    [63.7, 65.5, 67.4, 69.4, 71.4, 73.3, 75.1],
    [64.9, 66.8, 68.6, 70.7, 72.8, 74.6, 76.5],
    [66.0, 67.9, 69.8, 71.9, 74.0, 75.9, 77.8],
    [67.1, 69.0, 71.0, 73.1, 75.2, 77.2, 79.7],
    [68.2, 70.1, 72.0, 74.2, 76.4, 78.3, 80.2],
    [69.1, 71.1, 73.1, 75.3, 77.5, 79.5, 81.5],
    [70.1, 72.0, 74.1, 76.3, 78.5, 80.6, 82.5],
    [71.0, 73.0, 75.0, 77.3, 79.6, 81.6, 83.6],
    [71.9, 73.9, 76.0, 78.3, 80.6, 82.7, 84.7],
    [72.7, 74.8, 76.9, 79.2, 81.5, 83.6, 85.7],
    [73.6, 75.7, 77.8, 80.2, 82.6, 84.7, 86.8],
    [74.5, 76.6, 78.0, 81.2, 83.6, 85.8, 87.9],
    [75.4, 77.5, 79.7, 82.2, 84.7, 86.9, 89.0],
    [76.2, 78.5, 80.7, 83.2, 85.7, 87.9, 90.2],
    [76.9, 79.2, 81.5, 84.0, 86.5, 88.8, 91.1],
    [77.6, 79.9, 82.2, 84.8, 87.4, 89.7, 92.0],
    [78.1, 80.4, 82.7, 85.3, 87.9, 90.2, 92.5]], columns = [3, 10, 25, 50, 75, 90, 97])

tabla_talla_edad_girls = pd.DataFrame([
    [47.1, 48.7, 50.3, 52.1, 53.9, 55.5, 57.1],
    [50.8, 52.4, 54.1, 55.9, 57.7, 59.4, 61.0],
    [53.2, 54.9, 56.6, 58.4, 60.2, 61.9, 63.6],
    [55.5, 57.1, 58.8, 60.7, 62.6, 64.3, 65.9],
    [57.5, 59.2, 60.9, 62.8, 64.7, 66.4, 68.1],
    [59.5, 61.2, 63.0, 64.9, 66.8, 68.6, 70.3],
    [61.0, 62.7, 64.5, 66.4, 68.3, 70.1, 71.8],
    [62.3, 64.1, 65.8, 67.8, 69.8, 71.5, 73.3],
    [63.6, 65.4, 67.2, 69.2, 71.2, 73.0, 74.8],
    [64.9, 66.7, 68.5, 70.5, 72.5, 74.3, 76.1],
    [66.0, 67.8, 69.7, 71.7, 73.7, 75.6, 77.4],
    [67.1, 69.0, 70.8, 72.9, 75.0, 76.8, 78.7],
    [68.2, 70.0, 71.9, 74.0, 76.1, 78.0, 79.8],
    [69.2, 71.1, 73.0, 75.1, 77.2, 79.1, 81.0],
    [70.2, 72.1, 74.0, 76.2, 78.4, 80.3, 82.2],
    [71.1, 73.1, 75.0, 77.2, 79.4, 81.3, 83.3],
    [72.0, 73.9, 75.9, 78.1, 80.3, 82.3, 84.2],
    [72.8, 74.8, 76.8, 79.0, 81.2, 83.2, 85.2],
    [73.6, 75.6, 77.6, 79.9, 82.2, 84.2, 86.2],
    [74.5, 76.5, 78.5, 80.8, 83.1, 85.1, 87.1],
    [75.2, 77.2, 79.3, 81.6, 83.9, 86.0, 88.0],
    [75.9, 78.0, 80.1, 82.4, 84.7, 86.8, 88.9],
    [76.6, 78.6, 80.8, 83.1, 85.4, 87.6, 89.6],
    [77.1, 79.2, 81.3, 83.7, 86.1, 88.2]], columns = [3, 10, 25, 50, 75, 90, 97])
