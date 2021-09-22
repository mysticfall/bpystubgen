#!/usr/bin/env bash
# Loosely based on https://github.com/nutti/fake-bpy-module/blob/master/tools/utils/download_blender.sh
# Original script is written by Nutti(https://github.com/nutti), licensed under MIT.
# Usage: bash download_blender.sh 2.93 out
set -eEu

SUPPORTED_VERSIONS=("2.80" "2.81" "2.82" "2.83" "2.90" "2.91" "2.92" "2.93")

declare -A BLENDER_BINARY_URL=(
    ["v2.80"]="https://download.blender.org/release/Blender2.80/blender-2.80-linux-glibc217-x86_64.tar.bz2"
    ["v2.81"]="https://download.blender.org/release/Blender2.81/blender-2.81a-linux-glibc217-x86_64.tar.bz2"
    ["v2.82"]="https://download.blender.org/release/Blender2.82/blender-2.82a-linux64.tar.xz"
    ["v2.83"]="https://download.blender.org/release/Blender2.83/blender-2.83.17-linux-x64.tar.xz"
    ["v2.90"]="https://download.blender.org/release/Blender2.90/blender-2.90.1-linux64.tar.xz"
    ["v2.91"]="https://download.blender.org/release/Blender2.91/blender-2.91.2-linux64.tar.xz"
    ["v2.92"]="https://download.blender.org/release/Blender2.92/blender-2.92.0-linux64.tar.xz"
    ["v2.93"]="https://download.blender.org/release/Blender2.93/blender-2.93.4-linux-x64.tar.xz"
)

declare -A BLENDER_SOURCE_URL=(
    ["v2.80"]="https://download.blender.org/source/blender-2.80.tar.gz"
    ["v2.81"]="https://download.blender.org/source/blender-2.81a.tar.xz"
    ["v2.82"]="https://download.blender.org/source/blender-2.82a.tar.xz"
    ["v2.83"]="https://download.blender.org/source/blender-2.83.17.tar.xz"
    ["v2.90"]="https://download.blender.org/source/blender-2.90.1.tar.xz"
    ["v2.91"]="https://download.blender.org/source/blender-2.91.2.tar.xz"
    ["v2.92"]="https://download.blender.org/source/blender-2.92.0.tar.xz"
    ["v2.93"]="https://download.blender.org/source/blender-2.93.4.tar.xz"
)

function get_extractor() {
    local file_extension=${1}
    local extractor

    if [ "${file_extension}" = "gz" ]; then
        extractor="tar zxf"
    elif [[ "${file_extension}" = "bz2" || "${file_extension}" = "xz" ]]; then
        extractor="tar xf"
    fi
    echo "${extractor}"
}

function download_blender() {
    ver="${1}"
    output_dir="${2:?}/${ver}"

    bin_url="${BLENDER_BINARY_URL[${ver}]}"
    src_url="${BLENDER_SOURCE_URL[${ver}]}"

    bin_dir="${output_dir}/bin"
    src_dir="${output_dir}/src"

    rm -Rf "${output_dir}"
    mkdir -p "${bin_dir}"
    mkdir -p "${src_dir}"

    file_extension=${bin_url##*.}
    filename="$(basename "${bin_url}")"
    filepath="${output_dir}/${filename}"

    echo "Downloading Blender binary: ${bin_url}"

    curl --location --fail -s "${bin_url}" -o "${filepath}"

    local extractor

    extractor=$(get_extractor "${file_extension}")

    echo "Extracting Blender ${ver} to ${bin_dir}"

    $(get_extractor "${file_extension}") "${filepath}" -C "${bin_dir}" --strip-component=1

    file_extension=${src_url##*.}
    filename="$(basename "${src_url}")"
    filepath="${output_dir}/${filename}"

    echo "Downloading Blender source: ${src_url}"

    curl --location --fail -s "${src_url}" -o "${filepath}"

    echo "Extracting Blender source ${ver} to ${src_dir}"

    $(get_extractor "${file_extension}") "${filepath}" -C "${src_dir}" --strip-component=1
}

# check arguments
if [ $# -ne 2 ]; then
    echo "Usage: ./download_blender.sh <version> <output-dir>"
    exit 1
fi

version=${1}
output_dir=${2}

if [ -z "${output_dir}" ]; then
    echo "Error: <output-dir> cannot be empty. Use \".\" if you want to use the current folder."
    exit 1
fi

# check if the specified version is supported
supported=0

for v in "${SUPPORTED_VERSIONS[@]}"; do
    if [ "${v}" = "${version}" ]; then
        supported=1
    fi
done

if [ ${supported} -eq 0 ]; then
    echo "${version} is not supported."
    echo "Supported version is $("${SUPPORTED_VERSIONS[@]}")."
    exit 1
fi

ver=v${version}

download_blender "${ver}" "${output_dir}"
