<script>
  let selectedFile = null;
  let resultImageUrl = null;
  let loading = false;
  let error = null;

  function onFileChange(event) {
    selectedFile = event.target.files[0];
    resultImageUrl = null;
    error = null;
  }

  async function uploadImage() {
    if (!selectedFile) {
      error = "이미지를 선택하세요";
      return;
    }

    loading = true;
    error = null;

    const formData = new FormData();
    formData.append("file", selectedFile);

    try {
      const response = await fetch(
        "http://127.0.0.1:8000/api/v1/image/process",
        {
          method: "POST",
          body: formData
        }
      );

      if (!response.ok) {
        throw new Error("이미지 처리 실패");
      }

      const blob = await response.blob();
      resultImageUrl = URL.createObjectURL(blob);

    } catch (e) {
      error = e.message;
    } finally {
      loading = false;
    }
  }
</script>

<style>
  .container {
    max-width: 480px;
    margin: 40px auto;
    padding: 20px;
    border: 1px solid #ddd;
    border-radius: 8px;
  }

  img {
    max-width: 100%;
    margin-top: 16px;
    border-radius: 4px;
  }

  button {
    margin-top: 12px;
  }

  .error {
    color: red;
    margin-top: 8px;
  }
</style>

<div class="container">
  <h2>이미지 업로드</h2>

  <input type="file" accept="image/*" on:change={onFileChange} />

  <br />

  <button on:click={uploadImage} disabled={loading}>
    {loading ? "처리 중..." : "업로드"}
  </button>

  {#if error}
    <div class="error">{error}</div>
  {/if}

  {#if resultImageUrl}
    <h3>처리 결과</h3>
    <img src={resultImageUrl} alt="processed image" />
  {/if}
</div>