//
// Created by lap1dem on 9/7/22.
//

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "ECHAIM.h"

void pyDensityProfile(double *np_output, double lat, double lon, int year, int month, int day, int hour,
                      int min, int sec, int storm, int precip, int dregion, double *alt, int l1, int err) {

    double **output = densityProfile(&lat, &lon, &year, &month, &day, &hour, &min,
                                     &sec, storm, precip, dregion, 1, alt, l1, err);

    memcpy(np_output, output[0], sizeof(double) * l1);
    free(output);
}

void printnparray(double *np_output, int l1) {
    for (int j = 0; j < l1; j++) {
        printf("%f ", np_output[j]);
    }
    printf("\n");
}