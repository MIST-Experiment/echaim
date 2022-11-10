//
// Created by lap1dem on 9/7/22.
//

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "sqlite3.h"
#include "ECHAIM.h"
#include "getDir.h"
#include "global.h"

#include <omp.h>

void print_d_array(double *arr, int len) {
    for (int j = 0; j < len; j++) {
        printf("%f ", arr[j]);
    }
    printf("\n");
}

void print_i_array(int *arr, int len) {
    for (int j = 0; j < len; j++) {
        printf("%i ", arr[j]);
    }
    printf("\n");
}

void pyDensityProfile(double *np_output, char * datadir, double *lat, double *lon, int *year, int *month, int *day, int *hour,
                      int *min, int *sec, int storm, int precip, int dregion, int l0, double *alt, int l1, int err) {
    strcpy(DIR, datadir);
//    int nthreads, tid;
//    printf("%d", sqlite3_threadsafe());
//    nthreads = omp_get_num_threads();
//
//    #pragma omp parallel for default(none) shared(lat, lon, year, month, day, hour, min, \
//        sec, storm, precip, dregion, l0, alt, l1, err) private(nthreads, tid)
//    for (int i=0; i<l0; i++) {
//        tid = omp_get_thread_num();
//        printf("Hello World from thread = %d\n", tid);
//        if (tid == 0) {
//            nthreads = omp_get_num_threads();
//            printf("Number of threads = %d\n", nthreads);
//        }
        double **output = densityProfile(lat, lon, year, month, day, hour, min,
                                         sec, storm, precip, dregion, l0, alt, l1, err);
//    }
    memcpy(np_output, output[0], sizeof(double) * l1);
    free(output);
}