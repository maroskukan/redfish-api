# Mockup

## Environment

In order to create a custom mock environment using a Docker image provided by DMTF follow these steps:

```bash
# Downlaod and extract 
wget https://www.dmtf.org/sites/default/files/standards/documents/DSP2043_2020.4.zip
unzip -q DSP2043_2020.4.zip \
      -d .

# To unzip a specific mock only
unzip -q DSP2043_2020.4.zip \
      "DSP2043_2020.4/public-bladed/" \
      -d .

# Move to unzipped folder
cd DSP2043_2020.4

# Start Mockup server with volume mapping
docker run --rm \
           -p 8000:8000 \
           -v $PWD:/mockup \
           dmtf/redfish-mockup-server:latest \
           -D /mockup/public-bladed --short-form
```
