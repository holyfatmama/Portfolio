#include "helpers.h"
#include <math.h>
// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int h = 0; h < height; h++)
    {
        for (int w = 0; w < width; w++)
        {
            float red = image[h][w].rgbtRed;
            float blue = image[h][w].rgbtBlue;
            float green = image[h][w].rgbtGreen;

            int average = round ((red + blue + green)/3);

            image[h][w].rgbtRed = average;
            image[h][w].rgbtBlue = average;
            image[h][w].rgbtGreen = average;
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    for (int h = 0; h < height; h++)
    {
        for (int w = 0; w < width; w++)
        {
            float red = image[h][w].rgbtRed;
            float blue = image[h][w].rgbtBlue;
            float green = image[h][w].rgbtGreen;

            int sepiaRed = round((0.393 * red) + (0.769 * green) + (0.189 * blue));
            int sepiaBlue = round((0.349 * red) + (0.686 * green) + (0.168 * blue));
            int sepiaGreen = round((0.272 * red) + (0.534 * green) + (0.131 * blue));

            if (sepiaRed > 255)
            {
                sepiaRed = 255;
            }
            if (sepiaBlue > 255)
            {
                sepiaBlue = 255;
            }
            if (sepiaGreen > 255)
            {
                sepiaGreen = 255;
            }
            
            image[h][w].rgbtRed = sepiaRed;
            image[h][w].rgbtBlue = sepiaBlue;
            image[h][w].rgbtGreen = sepiaGreen;
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    return;
}
