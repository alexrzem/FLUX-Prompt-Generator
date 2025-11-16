import axios from 'axios'

const API_BASE_URL = '/api'

export const apiService = {
  // Image captioning using Florence-2
  async generateCaption(imageFile) {
    const formData = new FormData()
    formData.append('image', imageFile)

    try {
      const response = await axios.post(`${API_BASE_URL}/caption`, formData, {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      })
      return response.data.caption
    } catch (error) {
      console.error('Error generating caption:', error)
      throw error
    }
  },

  // Translate Korean to English
  async translateText(text, sourceLang = 'ko', targetLang = 'en') {
    try {
      const response = await axios.post(`${API_BASE_URL}/translate`, {
        text,
        source_lang: sourceLang,
        target_lang: targetLang
      })
      return response.data.translated_text
    } catch (error) {
      console.error('Error translating text:', error)
      throw error
    }
  },

  // Enhance prompt using OpenAI
  async enhancePrompt(prompt, options = {}) {
    const {
      happyTalkMode = false,
      compressionLevel = 'none',
      moviePosterMode = false,
      customInstruction = ''
    } = options

    try {
      const response = await axios.post(`${API_BASE_URL}/enhance`, {
        prompt,
        happy_talk_mode: happyTalkMode,
        compression_level: compressionLevel,
        movie_poster_mode: moviePosterMode,
        custom_instruction: customInstruction
      })
      return response.data.enhanced_prompt
    } catch (error) {
      console.error('Error enhancing prompt:', error)
      throw error
    }
  },

  // Check if OpenAI is available
  async checkOpenAIAvailability() {
    try {
      const response = await axios.get(`${API_BASE_URL}/openai-status`)
      return response.data.available
    } catch (error) {
      console.error('Error checking OpenAI availability:', error)
      return false
    }
  }
}

export default apiService
