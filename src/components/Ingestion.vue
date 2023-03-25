<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <b-alert class="alert-btn" v-model="showSuccess" variant="success" dismissible>
      File formated and saved!
    </b-alert>
    <b-alert class="alert-btn" v-model="showError" variant="danger" dismissible>
      Error, try again!
    </b-alert>
    <b-overlay :show="loading" rounded="sm">
      <div class="mt-4 d-flex w-100 justify-content-center">
        <div class="input-label">
          Xlsx file URL:
        </div>
        <div>
          <b-input v-model="fileURL" type="text"></b-input>
        </div>
      </div>
      <div>
        <b-button :disabled="fileURL.length < 3" @click="formatFile(fileURL)" class="mt-4" variant="outline-primary">Format and Analyze</b-button>
      </div>
  </b-overlay>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: 'HelloWorld',
  props: {
    msg: String
  },
  data() {
    return {
      fileURL: "",
      externalServiceURL: "https://v2.convertapi.com/convert/xlsx/to/csv?Secret=6mSJbYN6n0hm4GTj&StoreFile=true",
      apiServiceURL: "http://40.118.66.81",
      loading: false,
      showSuccess: false,
      showError: false
    }
  },
  methods: {
    async formatFile(file) {
      this.loading = true;
      let fileName = file.split("/");
      fileName = fileName[fileName.length - 1];
      try {
        let externalResponse = await axios.post(
          this.externalServiceURL,
          {
            File: file
          },
          {
            headers: {
              'Content-Type': 'multipart/form-data'
            },
          }
        );
        await axios.post(
          this.apiServiceURL + '/api/ingesta_archivos_xlsx',
          {
            fileData: {
              OriginalFile: fileName,
              Status: "Loaded",
              ...externalResponse.data.Files[0]
            }
          },
          {
            headers: {
              'Content-Type': 'application/json'
            },
          }
        );
        this.showSuccess = true;
      } catch (err) {
        this.showError = true;
      }
      this.loading = false;
      this.fileURL = "";
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.alert-btn ::v-deep .close {
  background-color: transparent;
  border: none;
  margin: 0 10px 0 10px;
}
.input-label {
  
  margin: auto 20px auto 20px;
}
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
