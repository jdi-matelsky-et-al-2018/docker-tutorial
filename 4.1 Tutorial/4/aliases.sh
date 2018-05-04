alias build-dicom-remap="docker build -t dicom-remap ."

docker run -v $(pwd)/myfile.dcm:/infile.dcm -v $(pwd):/mnt/vout dicom-remap
