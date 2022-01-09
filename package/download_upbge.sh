#!/usr/bin/env bash
# Loosely based on https://github.com/nutti/fake-bpy-module/blob/master/tools/utils/download_blender.sh
# Original script is written by Nutti(https://github.com/nutti), licensed under MIT.
# Usage: bash download_upbge.sh 0.30 out
set -eEu

SUPPORTED_VERSIONS=("0.3.0")

declare -A BLENDER_BINARY_URL=(
    ["v0.3.0"]="https://github.com/UPBGE/upbge/releases/download/v0.30/UPBGE-0.30-linux-x86_64.tar.xz"
)

declare -A BLENDER_SOURCE_URL=(
    ["v0.3.0"]="https://github.com/UPBGE/upbge/archive/refs/tags/v0.30.zip"
)

function download_upbge() {
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

    echo "Downloading UPBGE binary: ${bin_url}"

    curl --location --fail -s "${bin_url}" -o "${filepath}"

    echo "Extracting UPBGE ${ver} to ${bin_dir}"

    tar xf "${filepath}" -C "${bin_dir}" --strip-component=1

    file_extension=${src_url##*.}
    filename="$(basename "${src_url}")"
    filepath="${output_dir}/${filename}"

    echo "Downloading UPBGE source: ${src_url}"

    curl --location --fail -s "${src_url}" -o "${filepath}"

    echo "Extracting UPBGE source ${ver} to ${src_dir}"

    unzip -d "${src_dir}" "${filepath}" && f=("${src_dir}"/*) && mv "${src_dir}"/*/* "${src_dir}" && rm -Rf "${f[@]}"
}

# check arguments
if [ $# -ne 2 ]; then
    echo "Usage: ./download_upbge.sh <version> <output-dir>"
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
    echo "Supported version is ("${SUPPORTED_VERSIONS[@]}")."
    exit 1
fi

ver=v${version}

download_upbge "${ver}" "${output_dir}"
