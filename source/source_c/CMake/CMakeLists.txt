cmake_minimum_required (VERSION 3.6.2)

set (project_name
	ECHAIM)

#Project name
project (${project_name})

#message ("${PROJECT_SOURCE_DIR}")

#include_directories (../include "${PROJECT_SOURCE_DIR}/source")

include_directories (../include)

set(LIB_SOURCES
	../lib/aacgmlib_v2.c
	../lib/astalglib.c
	../lib/calcBot.c
	../lib/calcHmF1.c
	../lib/calcMF2.c
	../lib/calcPert.c
	../lib/calcTop.c
	../lib/date.c
	../lib/densityFunc.c
	../lib/densityPath.c
	../lib/densityProfile.c
	../lib/errorCodes.c
	../lib/genmag.c
	../lib/getCoefs.c
	../lib/getDir.c
	../lib/getIndices.c
	../lib/getMagCoords.c
	../lib/igrflib.c
	../lib/mathlib.c
	../lib/maxIndices.c
	../lib/mlt_v2.c
	../lib/otherIndices.c
	../lib/parameterAE.c
	../lib/parameterBot.c
	../lib/parameterHmF1.c
	../lib/parameterHmF2.c
	../lib/parameterNmF2.c
	../lib/parameterPert.c
	../lib/parameterTop.c
	../lib/prepInd.c
	../lib/rtime.c
	../lib/singleOutput.c
	../lib/sqlite3.c
	../lib/calcPrecip.c
	../lib/ECHAIMFIRI2018.c
	../lib/energyFluxModel.c
	../lib/energyFunctions.c
	../lib/FIRITools.c
	../lib/getFIRI.c
	../lib/getPrecipModel.c
	../lib/nrlmsise-00_data.c
	../lib/nrlmsise00.c
	../lib/runNRLMSISE.c
	../lib/updateLocalDB.c ../lib/python_api.c)


#create the shared library
add_library (${project_name} SHARED ${LIB_SOURCES}) 

#Link the curl library
target_link_libraries(${project_name} curl)

#change the runtime output directory
get_filename_component(PARENT_DIR . DIRECTORY)
message(${PARENT_DIR})
set( CMAKE_RUNTIME_OUTPUT_DIRECTORY ${PARENT_DIR})


configure_file(../User/ECHAIM.c ../lib/ECHAIM.c COPYONLY)

add_executable (ECHAIM_User ../lib/ECHAIM.c)
target_link_libraries (ECHAIM_User ${project_name})

#link libraries to executable
find_package (Threads)
target_link_libraries (ECHAIM_User ${CMAKE_THREAD_LIBS_INIT})
target_link_libraries (ECHAIM_User ${CMAKE_DL_LIBS})
target_link_libraries(${project_name} m)

#set the compiler C99 flag
set_property(TARGET ${project_name} PROPERTY C_STANDARD 99)
set_property(TARGET ECHAIM_User PROPERTY C_STANDARD 99)

#Install the input file for User front end
configure_file(../User/ECHAIMInputs.dat ../etc/ECHAIMInputs.dat COPYONLY)

#Write the configECHAIM.dat file
file(WRITE "../configECHAIM.dat" "\#This is the directory which contains the ECHAIM database (.DB) file,
\#the AACGM coefficient file, the COEFS database, and downloaded indices.
${PARENT_DIR}/etc" \n)
