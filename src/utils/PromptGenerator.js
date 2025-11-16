export class PromptGenerator {
  constructor() {
    this.data = {}
    this.loaded = false
  }

  async loadData() {
    if (this.loaded) return

    const files = [
      'artform', 'artist', 'background', 'body_types', 'clothing',
      'composition', 'default_tags', 'device', 'digital_artform',
      'hairstyles', 'lighting', 'photo_framing', 'photo_type',
      'photographer', 'photography_styles', 'place', 'pose', 'roles',
      'additional_details'
    ]

    try {
      await Promise.all(
        files.map(async (file) => {
          const response = await fetch(`/data/${file}.json`)
          this.data[file] = await response.json()
        })
      )
      this.loaded = true
    } catch (error) {
      console.error('Error loading data files:', error)
      throw error
    }
  }

  getRandomElement(array) {
    if (!array || array.length === 0) return ''
    return array[Math.floor(Math.random() * array.length)]
  }

  getRandomElements(array, count = 1) {
    if (!array || array.length === 0) return []
    const shuffled = [...array].sort(() => 0.5 - Math.random())
    return shuffled.slice(0, Math.min(count, array.length))
  }

  generatePrompt(options = {}) {
    const {
      seed = Date.now(),
      customPrompt = '',
      subject = '',
      artform = 'random',
      photoType = 'random',
      bodyType = 'random',
      role = 'random',
      hairstyle = 'random',
      clothing = 'random',
      pose = 'random',
      background = 'random',
      lighting = 'random',
      composition = 'random',
      place = 'random',
      photographer = 'random',
      artist = 'random',
      device = 'random',
      digitalArtform = 'random',
      additionalDetails = [],
      photographyStyle = 'random',
      photoFraming = 'random',
      useDefaultTags = true
    } = options

    // Set seed for reproducibility
    this.setSeed(seed)

    const parts = []

    // Add custom prompt
    if (customPrompt && customPrompt.trim()) {
      parts.push(customPrompt.trim())
    }

    // Add subject
    if (subject && subject.trim()) {
      parts.push(subject.trim())
    }

    // Add artform
    if (artform !== 'none') {
      const artformValue = artform === 'random'
        ? this.getRandomElement(this.data.artform)
        : artform
      if (artformValue) parts.push(artformValue)
    }

    // Add photo type
    if (photoType !== 'none') {
      const photoTypeValue = photoType === 'random'
        ? this.getRandomElement(this.data.photo_type)
        : photoType
      if (photoTypeValue) parts.push(photoTypeValue)
    }

    // Add body type
    if (bodyType !== 'none') {
      const bodyTypeValue = bodyType === 'random'
        ? this.getRandomElement(this.data.body_types)
        : bodyType
      if (bodyTypeValue) parts.push(bodyTypeValue)
    }

    // Add role
    if (role !== 'none') {
      const roleValue = role === 'random'
        ? this.getRandomElement(this.data.roles)
        : role
      if (roleValue) parts.push(roleValue)
    }

    // Add hairstyle
    if (hairstyle !== 'none') {
      const hairstyleValue = hairstyle === 'random'
        ? this.getRandomElement(this.data.hairstyles)
        : hairstyle
      if (hairstyleValue) parts.push(hairstyleValue)
    }

    // Add clothing
    if (clothing !== 'none') {
      const clothingValue = clothing === 'random'
        ? this.getRandomElement(this.data.clothing)
        : clothing
      if (clothingValue) parts.push(clothingValue)
    }

    // Add pose
    if (pose !== 'none') {
      const poseValue = pose === 'random'
        ? this.getRandomElement(this.data.pose)
        : pose
      if (poseValue) parts.push(poseValue)
    }

    // Add background
    if (background !== 'none') {
      const backgroundValue = background === 'random'
        ? this.getRandomElement(this.data.background)
        : background
      if (backgroundValue) parts.push(backgroundValue)
    }

    // Add lighting
    if (lighting !== 'none') {
      const lightingValue = lighting === 'random'
        ? this.getRandomElement(this.data.lighting)
        : lighting
      if (lightingValue) parts.push(lightingValue)
    }

    // Add composition
    if (composition !== 'none') {
      const compositionValue = composition === 'random'
        ? this.getRandomElement(this.data.composition)
        : composition
      if (compositionValue) parts.push(compositionValue)
    }

    // Add place
    if (place !== 'none') {
      const placeValue = place === 'random'
        ? this.getRandomElement(this.data.place)
        : place
      if (placeValue) parts.push(placeValue)
    }

    // Add photographer
    if (photographer !== 'none') {
      const photographerValue = photographer === 'random'
        ? this.getRandomElement(this.data.photographer)
        : photographer
      if (photographerValue) parts.push(`by ${photographerValue}`)
    }

    // Add artist
    if (artist !== 'none') {
      const artistValue = artist === 'random'
        ? this.getRandomElement(this.data.artist)
        : artist
      if (artistValue) parts.push(`by ${artistValue}`)
    }

    // Add device
    if (device !== 'none') {
      const deviceValue = device === 'random'
        ? this.getRandomElement(this.data.device)
        : device
      if (deviceValue) parts.push(deviceValue)
    }

    // Add digital artform
    if (digitalArtform !== 'none') {
      const digitalArtformValue = digitalArtform === 'random'
        ? this.getRandomElement(this.data.digital_artform)
        : digitalArtform
      if (digitalArtformValue) parts.push(digitalArtformValue)
    }

    // Add photography style
    if (photographyStyle !== 'none') {
      const photographyStyleValue = photographyStyle === 'random'
        ? this.getRandomElement(this.data.photography_styles)
        : photographyStyle
      if (photographyStyleValue) parts.push(photographyStyleValue)
    }

    // Add photo framing
    if (photoFraming !== 'none') {
      const photoFramingValue = photoFraming === 'random'
        ? this.getRandomElement(this.data.photo_framing)
        : photoFraming
      if (photoFramingValue) parts.push(photoFramingValue)
    }

    // Add additional details
    if (additionalDetails && additionalDetails.length > 0) {
      parts.push(...additionalDetails)
    }

    // Add default tags
    if (useDefaultTags) {
      const defaultTags = this.data.default_tags || []
      parts.push(...defaultTags)
    }

    return parts.filter(p => p && p.trim()).join(', ')
  }

  setSeed(seed) {
    // Simple seeded random number generator
    this._seed = seed
    this._random = this.mulberry32(seed)
  }

  mulberry32(a) {
    return function() {
      let t = a += 0x6D2B79F5
      t = Math.imul(t ^ t >>> 15, t | 1)
      t ^= t + Math.imul(t ^ t >>> 7, t | 61)
      return ((t ^ t >>> 14) >>> 0) / 4294967296
    }
  }

  // Generate tokenized outputs for different CLIP models
  generateTokenizedOutputs(prompt) {
    // These would normally use actual tokenizers
    // For now, we'll just return the prompt with markers
    return {
      t5xxl: this.tokenizeForT5(prompt),
      clipL: this.tokenizeForCLIPL(prompt),
      clipG: this.tokenizeForCLIPG(prompt)
    }
  }

  tokenizeForT5(prompt) {
    // Simplified tokenization - in production, use actual T5 tokenizer
    return `[T5XXL] ${prompt}`
  }

  tokenizeForCLIPL(prompt) {
    // Simplified tokenization - in production, use actual CLIP L tokenizer
    const parts = prompt.split('BREAK_CLIPL')
    return `[CLIP-L] ${parts[0] || prompt}`
  }

  tokenizeForCLIPG(prompt) {
    // Simplified tokenization - in production, use actual CLIP G tokenizer
    const parts = prompt.split('BREAK_CLIPG')
    return `[CLIP-G] ${parts[0] || prompt}`
  }
}

export default PromptGenerator
