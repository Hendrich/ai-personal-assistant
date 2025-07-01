# ai-financial-advisor

## Dokumentasi

### Alur Kerja Agent & Arsitektur

1. **User** memberikan pertanyaan atau permintaan terkait investasi.
2. **Agent** menerima input dan menyimpan riwayat percakapan menggunakan episodic memory.
3. **Agent** memproses input dengan LLM (OpenAI GPT) dan dapat memanggil tool (misal: kalkulator return investasi) jika diperlukan.
4. **Agent** memberikan saran atau jawaban ke user berdasarkan hasil reasoning LLM, memory, dan tool.

**Arsitektur:**

- Prompt (instruksi sistem)
- Memory (episodic)
- Tool/function calling
- LLM (OpenAI)
- Agent loop (observe → decide → act)

### Pendekatan Memory (Episodic / Semantic)

- **Episodic Memory:**
  - Menggunakan `ConversationBufferMemory` dari Langchain untuk menyimpan riwayat percakapan (chat history) sehingga agent dapat merespons dengan konteks percakapan sebelumnya.
- **Semantic Memory:**
  - Belum diimplementasikan pada versi ini. Dapat ditambah dengan knowledge base eksternal jika dibutuhkan.

### RAG / Prompt Strategy

- **Prompt Strategy:**
  - Menggunakan prompt sistem yang mengarahkan LLM untuk bertindak sebagai financial advisor yang edukatif dan logis.
- **RAG (Retrieval Augmented Generation):**
  - Belum diimplementasikan. Dapat ditambah dengan integrasi knowledge base atau API eksternal untuk memperkaya jawaban agent.

### Hasil & Refleksi

- **Hasil:**
  - Agent dapat menjawab pertanyaan investasi dan menghitung return investasi dengan tool sederhana.
  - Memory percakapan berjalan baik (episodic).
- **Refleksi:**
  - Kendala: Integrasi API eksternal (misal data saham) memerlukan tool tambahan dan API key.
  - Solusi: Dapat menambah tool baru di Langchain dan menambah semantic memory/RAG jika ingin knowledge base lebih kaya.
