# generated from ament/cmake/core/templates/nameConfig.cmake.in

# prevent multiple inclusion
if(_materialdetect_CONFIG_INCLUDED)
  # ensure to keep the found flag the same
  if(NOT DEFINED materialdetect_FOUND)
    # explicitly set it to FALSE, otherwise CMake will set it to TRUE
    set(materialdetect_FOUND FALSE)
  elseif(NOT materialdetect_FOUND)
    # use separate condition to avoid uninitialized variable warning
    set(materialdetect_FOUND FALSE)
  endif()
  return()
endif()
set(_materialdetect_CONFIG_INCLUDED TRUE)

# output package information
if(NOT materialdetect_FIND_QUIETLY)
  message(STATUS "Found materialdetect: 0.0.0 (${materialdetect_DIR})")
endif()

# warn when using a deprecated package
if(NOT "" STREQUAL "")
  set(_msg "Package 'materialdetect' is deprecated")
  # append custom deprecation text if available
  if(NOT "" STREQUAL "TRUE")
    set(_msg "${_msg} ()")
  endif()
  # optionally quiet the deprecation message
  if(NOT ${materialdetect_DEPRECATED_QUIET})
    message(DEPRECATION "${_msg}")
  endif()
endif()

# flag package as ament-based to distinguish it after being find_package()-ed
set(materialdetect_FOUND_AMENT_PACKAGE TRUE)

# include all config extra files
set(_extras "")
foreach(_extra ${_extras})
  include("${materialdetect_DIR}/${_extra}")
endforeach()
