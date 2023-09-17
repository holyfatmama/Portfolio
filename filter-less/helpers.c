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
            float originalRed = image[h][w].rgbtRed;
            float originalGreen = image[h][w].rgbtGreen;
            float originalBlue = image[h][w].rgbtBlue;

            int sepiaRed = round(0.393 * originalRed + 0.769 * originalGreen + 0.189 * originalBlue);
            int sepiaGreen = round(0.349 * originalRed + 0.686 * originalGreen + 0.168 * originalBlue);
            int sepiaBlue = round(0.272 * originalRed + 0.534 * originalGreen + 0.131 * originalBlue);

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
    int reflect = (height/2);
    for (int h = 0; h < height; h++)
    {
        for (int w = 0; w < reflect; w++)
        {
            int temp = image[h][w];
            image[h][w] = image[h][width - (w + 1)];
            image[h][width - (w+1)] = temp;
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    return;
}
