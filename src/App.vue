<template>
  <div class="min-h-screen bg-gray-50">
    <Toast />

    <!-- Header -->
    <div class="gradient-header mb-6">
      <h1 class="text-3xl font-bold text-center">FLUX Prompt Generator</h1>
      <p class="text-center text-sm mt-2 opacity-90">Generate detailed prompts for FLUX image generation</p>
    </div>

    <!-- Main Grid Layout -->
    <div class="container mx-auto px-4">
      <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">

        <!-- Left Panel: Settings -->
        <div class="space-y-4">
          <Card>
            <template #header>
              <div class="bg-blue-600 text-white p-4 rounded-t-lg">
                <h2 class="text-xl font-semibold">Settings</h2>
              </div>
            </template>
            <template #content>
              <!-- Seed Control -->
              <div class="mb-4">
                <label class="block text-sm font-medium mb-2">Seed (for reproducibility)</label>
                <InputNumber
                  v-model="settings.seed"
                  :useGrouping="false"
                  class="w-full"
                />
              </div>

              <!-- Custom Prompt -->
              <div class="mb-4">
                <label class="block text-sm font-medium mb-2">Custom Prompt (Korean supported)</label>
                <Textarea
                  v-model="settings.customPrompt"
                  rows="3"
                  class="w-full"
                  placeholder="Enter your custom prompt here..."
                />
              </div>

              <!-- Subject -->
              <div class="mb-4">
                <label class="block text-sm font-medium mb-2">Subject</label>
                <InputText
                  v-model="settings.subject"
                  class="w-full"
                  placeholder="e.g., a young woman, a warrior, etc."
                />
              </div>

              <!-- Use Default Tags -->
              <div class="mb-4">
                <div class="flex items-center">
                  <Checkbox v-model="settings.useDefaultTags" :binary="true" inputId="defaultTags" />
                  <label for="defaultTags" class="ml-2">Use default quality tags</label>
                </div>
              </div>

              <!-- Artform Selection Accordion -->
              <Accordion :multiple="true" class="mb-4">
                <AccordionTab header="Artform & Photo Type">
                  <div class="space-y-4">
                    <div>
                      <label class="block text-sm font-medium mb-2">Artform</label>
                      <Dropdown
                        v-model="settings.artform"
                        :options="dropdownOptions.artform"
                        optionLabel="label"
                        optionValue="value"
                        placeholder="Select artform"
                        class="w-full"
                      />
                    </div>
                    <div>
                      <label class="block text-sm font-medium mb-2">Photo Type</label>
                      <Dropdown
                        v-model="settings.photoType"
                        :options="dropdownOptions.photoType"
                        optionLabel="label"
                        optionValue="value"
                        placeholder="Select photo type"
                        class="w-full"
                      />
                    </div>
                    <div>
                      <label class="block text-sm font-medium mb-2">Digital Artform</label>
                      <Dropdown
                        v-model="settings.digitalArtform"
                        :options="dropdownOptions.digitalArtform"
                        optionLabel="label"
                        optionValue="value"
                        placeholder="Select digital artform"
                        class="w-full"
                      />
                    </div>
                  </div>
                </AccordionTab>

                <AccordionTab header="Character Settings">
                  <div class="space-y-4">
                    <div>
                      <label class="block text-sm font-medium mb-2">Body Type</label>
                      <Dropdown
                        v-model="settings.bodyType"
                        :options="dropdownOptions.bodyType"
                        optionLabel="label"
                        optionValue="value"
                        placeholder="Select body type"
                        class="w-full"
                      />
                    </div>
                    <div>
                      <label class="block text-sm font-medium mb-2">Role</label>
                      <Dropdown
                        v-model="settings.role"
                        :options="dropdownOptions.role"
                        optionLabel="label"
                        optionValue="value"
                        placeholder="Select role"
                        class="w-full"
                      />
                    </div>
                    <div>
                      <label class="block text-sm font-medium mb-2">Hairstyle</label>
                      <Dropdown
                        v-model="settings.hairstyle"
                        :options="dropdownOptions.hairstyle"
                        optionLabel="label"
                        optionValue="value"
                        placeholder="Select hairstyle"
                        class="w-full"
                      />
                    </div>
                    <div>
                      <label class="block text-sm font-medium mb-2">Clothing</label>
                      <Dropdown
                        v-model="settings.clothing"
                        :options="dropdownOptions.clothing"
                        optionLabel="label"
                        optionValue="value"
                        placeholder="Select clothing"
                        class="w-full"
                      />
                    </div>
                    <div>
                      <label class="block text-sm font-medium mb-2">Pose</label>
                      <Dropdown
                        v-model="settings.pose"
                        :options="dropdownOptions.pose"
                        optionLabel="label"
                        optionValue="value"
                        placeholder="Select pose"
                        class="w-full"
                      />
                    </div>
                  </div>
                </AccordionTab>

                <AccordionTab header="Scene Settings">
                  <div class="space-y-4">
                    <div>
                      <label class="block text-sm font-medium mb-2">Background</label>
                      <Dropdown
                        v-model="settings.background"
                        :options="dropdownOptions.background"
                        optionLabel="label"
                        optionValue="value"
                        placeholder="Select background"
                        class="w-full"
                      />
                    </div>
                    <div>
                      <label class="block text-sm font-medium mb-2">Place</label>
                      <Dropdown
                        v-model="settings.place"
                        :options="dropdownOptions.place"
                        optionLabel="label"
                        optionValue="value"
                        placeholder="Select place"
                        class="w-full"
                      />
                    </div>
                    <div>
                      <label class="block text-sm font-medium mb-2">Lighting</label>
                      <Dropdown
                        v-model="settings.lighting"
                        :options="dropdownOptions.lighting"
                        optionLabel="label"
                        optionValue="value"
                        placeholder="Select lighting"
                        class="w-full"
                      />
                    </div>
                  </div>
                </AccordionTab>

                <AccordionTab header="Style & Technical">
                  <div class="space-y-4">
                    <div>
                      <label class="block text-sm font-medium mb-2">Composition</label>
                      <Dropdown
                        v-model="settings.composition"
                        :options="dropdownOptions.composition"
                        optionLabel="label"
                        optionValue="value"
                        placeholder="Select composition"
                        class="w-full"
                      />
                    </div>
                    <div>
                      <label class="block text-sm font-medium mb-2">Photography Style</label>
                      <Dropdown
                        v-model="settings.photographyStyle"
                        :options="dropdownOptions.photographyStyle"
                        optionLabel="label"
                        optionValue="value"
                        placeholder="Select photography style"
                        class="w-full"
                      />
                    </div>
                    <div>
                      <label class="block text-sm font-medium mb-2">Photo Framing</label>
                      <Dropdown
                        v-model="settings.photoFraming"
                        :options="dropdownOptions.photoFraming"
                        optionLabel="label"
                        optionValue="value"
                        placeholder="Select photo framing"
                        class="w-full"
                      />
                    </div>
                    <div>
                      <label class="block text-sm font-medium mb-2">Photographer</label>
                      <Dropdown
                        v-model="settings.photographer"
                        :options="dropdownOptions.photographer"
                        optionLabel="label"
                        optionValue="value"
                        placeholder="Select photographer"
                        class="w-full"
                      />
                    </div>
                    <div>
                      <label class="block text-sm font-medium mb-2">Artist</label>
                      <Dropdown
                        v-model="settings.artist"
                        :options="dropdownOptions.artist"
                        optionLabel="label"
                        optionValue="value"
                        placeholder="Select artist"
                        class="w-full"
                      />
                    </div>
                    <div>
                      <label class="block text-sm font-medium mb-2">Device</label>
                      <Dropdown
                        v-model="settings.device"
                        :options="dropdownOptions.device"
                        optionLabel="label"
                        optionValue="value"
                        placeholder="Select device"
                        class="w-full"
                      />
                    </div>
                  </div>
                </AccordionTab>
              </Accordion>

              <Button
                @click="generatePrompt"
                label="Generate Prompt"
                icon="pi pi-sparkles"
                class="w-full p-button-lg"
                :loading="generating"
              />
            </template>
          </Card>
        </div>

        <!-- Middle Panel: Image & Prompt Output -->
        <div class="space-y-4">
          <Card>
            <template #header>
              <div class="bg-green-600 text-white p-4 rounded-t-lg">
                <h2 class="text-xl font-semibold">Image Caption Generator</h2>
              </div>
            </template>
            <template #content>
              <FileUpload
                mode="basic"
                accept="image/*"
                :maxFileSize="10000000"
                @select="onImageSelect"
                :auto="true"
                chooseLabel="Upload Image"
                class="mb-4"
              />

              <div v-if="uploadedImage" class="mb-4">
                <img :src="uploadedImage" alt="Uploaded" class="w-full rounded-lg" />
              </div>

              <div v-if="generatedCaption" class="mb-4">
                <label class="block text-sm font-medium mb-2">Generated Caption</label>
                <Textarea
                  v-model="generatedCaption"
                  rows="4"
                  class="w-full"
                  readonly
                />
                <Button
                  @click="useCaption"
                  label="Use as Custom Prompt"
                  icon="pi pi-check"
                  class="w-full mt-2"
                  size="small"
                />
              </div>
            </template>
          </Card>

          <Card>
            <template #header>
              <div class="bg-purple-600 text-white p-4 rounded-t-lg">
                <h2 class="text-xl font-semibold">Generated Prompt</h2>
              </div>
            </template>
            <template #content>
              <Textarea
                v-model="generatedPrompt"
                rows="8"
                class="w-full mb-4"
                placeholder="Your generated prompt will appear here..."
              />

              <Button
                @click="copyPrompt"
                label="Copy Prompt"
                icon="pi pi-copy"
                class="w-full"
              />

              <!-- Tokenized Outputs -->
              <div v-if="showTokenizedOutputs" class="mt-4 space-y-3">
                <div>
                  <label class="block text-sm font-medium mb-1">T5XXL Tokens</label>
                  <Textarea
                    v-model="tokenizedOutputs.t5xxl"
                    rows="3"
                    class="w-full text-xs"
                    readonly
                  />
                </div>
                <div>
                  <label class="block text-sm font-medium mb-1">CLIP-L Tokens</label>
                  <Textarea
                    v-model="tokenizedOutputs.clipL"
                    rows="3"
                    class="w-full text-xs"
                    readonly
                  />
                </div>
                <div>
                  <label class="block text-sm font-medium mb-1">CLIP-G Tokens</label>
                  <Textarea
                    v-model="tokenizedOutputs.clipG"
                    rows="3"
                    class="w-full text-xs"
                    readonly
                  />
                </div>
              </div>
            </template>
          </Card>
        </div>

        <!-- Right Panel: OpenAI Enhancement -->
        <div class="space-y-4">
          <Card>
            <template #header>
              <div class="bg-orange-600 text-white p-4 rounded-t-lg">
                <h2 class="text-xl font-semibold">AI Enhancement (OpenAI)</h2>
              </div>
            </template>
            <template #content>
              <div v-if="!openaiAvailable" class="mb-4 p-3 bg-yellow-100 border-l-4 border-yellow-500 text-yellow-700">
                <p class="text-sm">OpenAI API is not configured. Enhancement features are disabled.</p>
              </div>

              <div class="space-y-4">
                <div class="flex items-center">
                  <Checkbox
                    v-model="enhancementSettings.happyTalkMode"
                    :binary="true"
                    inputId="happyTalk"
                    :disabled="!openaiAvailable"
                  />
                  <label for="happyTalk" class="ml-2">Happy Talk Mode</label>
                </div>

                <div class="flex items-center">
                  <Checkbox
                    v-model="enhancementSettings.moviePosterMode"
                    :binary="true"
                    inputId="moviePoster"
                    :disabled="!openaiAvailable"
                  />
                  <label for="moviePoster" class="ml-2">Movie Poster Mode</label>
                </div>

                <div>
                  <label class="block text-sm font-medium mb-2">Compression Level</label>
                  <Dropdown
                    v-model="enhancementSettings.compressionLevel"
                    :options="compressionLevels"
                    optionLabel="label"
                    optionValue="value"
                    placeholder="Select compression"
                    class="w-full"
                    :disabled="!openaiAvailable"
                  />
                </div>

                <div>
                  <label class="block text-sm font-medium mb-2">Custom Instructions</label>
                  <Textarea
                    v-model="enhancementSettings.customInstruction"
                    rows="4"
                    class="w-full"
                    placeholder="Additional instructions for enhancement..."
                    :disabled="!openaiAvailable"
                  />
                </div>

                <Button
                  @click="enhancePrompt"
                  label="Enhance with AI"
                  icon="pi pi-bolt"
                  class="w-full"
                  :disabled="!openaiAvailable || !generatedPrompt"
                  :loading="enhancing"
                />

                <div v-if="enhancedPrompt" class="mt-4">
                  <label class="block text-sm font-medium mb-2">Enhanced Prompt</label>
                  <Textarea
                    v-model="enhancedPrompt"
                    rows="6"
                    class="w-full"
                  />
                  <Button
                    @click="copyEnhancedPrompt"
                    label="Copy Enhanced Prompt"
                    icon="pi pi-copy"
                    class="w-full mt-2"
                    size="small"
                  />
                </div>
              </div>
            </template>
          </Card>

          <!-- Info Card -->
          <Card>
            <template #content>
              <div class="text-sm text-gray-600 space-y-2">
                <p><strong>Tip:</strong> Use "random" to let the generator pick values automatically.</p>
                <p><strong>Korean Support:</strong> Type Korean text in the custom prompt field - it will be automatically translated.</p>
                <p><strong>Seed:</strong> Use the same seed value to generate identical prompts with the same settings.</p>
              </div>
            </template>
          </Card>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, reactive, onMounted } from 'vue'
import { useToast } from 'primevue/usetoast'
import PromptGenerator from './utils/PromptGenerator'
import apiService from './services/api'

export default {
  name: 'App',
  setup() {
    const toast = useToast()
    const promptGenerator = new PromptGenerator()

    const generating = ref(false)
    const enhancing = ref(false)
    const openaiAvailable = ref(false)
    const uploadedImage = ref(null)
    const generatedCaption = ref('')
    const generatedPrompt = ref('')
    const enhancedPrompt = ref('')
    const showTokenizedOutputs = ref(false)

    const settings = reactive({
      seed: Date.now(),
      customPrompt: '',
      subject: '',
      artform: 'random',
      photoType: 'random',
      bodyType: 'random',
      role: 'random',
      hairstyle: 'random',
      clothing: 'random',
      pose: 'random',
      background: 'random',
      lighting: 'random',
      composition: 'random',
      place: 'random',
      photographer: 'random',
      artist: 'random',
      device: 'random',
      digitalArtform: 'random',
      photographyStyle: 'random',
      photoFraming: 'random',
      useDefaultTags: true
    })

    const enhancementSettings = reactive({
      happyTalkMode: false,
      compressionLevel: 'none',
      moviePosterMode: false,
      customInstruction: ''
    })

    const dropdownOptions = reactive({
      artform: [],
      photoType: [],
      bodyType: [],
      role: [],
      hairstyle: [],
      clothing: [],
      pose: [],
      background: [],
      lighting: [],
      composition: [],
      place: [],
      photographer: [],
      artist: [],
      device: [],
      digitalArtform: [],
      photographyStyle: [],
      photoFraming: []
    })

    const tokenizedOutputs = reactive({
      t5xxl: '',
      clipL: '',
      clipG: ''
    })

    const compressionLevels = [
      { label: 'None', value: 'none' },
      { label: 'Light', value: 'light' },
      { label: 'Medium', value: 'medium' },
      { label: 'Heavy', value: 'heavy' }
    ]

    const createDropdownOptions = (dataArray, category) => {
      const options = [
        { label: 'None', value: 'none' },
        { label: 'Random', value: 'random' }
      ]

      if (dataArray && Array.isArray(dataArray)) {
        dataArray.forEach(item => {
          options.push({ label: item, value: item })
        })
      }

      return options
    }

    const loadData = async () => {
      try {
        await promptGenerator.loadData()

        // Populate dropdown options
        dropdownOptions.artform = createDropdownOptions(promptGenerator.data.artform)
        dropdownOptions.photoType = createDropdownOptions(promptGenerator.data.photo_type)
        dropdownOptions.bodyType = createDropdownOptions(promptGenerator.data.body_types)
        dropdownOptions.role = createDropdownOptions(promptGenerator.data.roles)
        dropdownOptions.hairstyle = createDropdownOptions(promptGenerator.data.hairstyles)
        dropdownOptions.clothing = createDropdownOptions(promptGenerator.data.clothing)
        dropdownOptions.pose = createDropdownOptions(promptGenerator.data.pose)
        dropdownOptions.background = createDropdownOptions(promptGenerator.data.background)
        dropdownOptions.lighting = createDropdownOptions(promptGenerator.data.lighting)
        dropdownOptions.composition = createDropdownOptions(promptGenerator.data.composition)
        dropdownOptions.place = createDropdownOptions(promptGenerator.data.place)
        dropdownOptions.photographer = createDropdownOptions(promptGenerator.data.photographer)
        dropdownOptions.artist = createDropdownOptions(promptGenerator.data.artist)
        dropdownOptions.device = createDropdownOptions(promptGenerator.data.device)
        dropdownOptions.digitalArtform = createDropdownOptions(promptGenerator.data.digital_artform)
        dropdownOptions.photographyStyle = createDropdownOptions(promptGenerator.data.photography_styles)
        dropdownOptions.photoFraming = createDropdownOptions(promptGenerator.data.photo_framing)

        toast.add({ severity: 'success', summary: 'Ready', detail: 'Data loaded successfully', life: 3000 })
      } catch (error) {
        toast.add({ severity: 'error', summary: 'Error', detail: 'Failed to load data', life: 5000 })
      }
    }

    const checkOpenAI = async () => {
      openaiAvailable.value = await apiService.checkOpenAIAvailability()
    }

    const generatePrompt = async () => {
      generating.value = true
      try {
        // Check if custom prompt contains Korean and translate if needed
        let customPrompt = settings.customPrompt
        if (customPrompt && /[\u3131-\uD79D]/.test(customPrompt)) {
          try {
            customPrompt = await apiService.translateText(customPrompt)
            toast.add({ severity: 'info', summary: 'Translated', detail: 'Korean text translated to English', life: 3000 })
          } catch (error) {
            console.error('Translation failed:', error)
          }
        }

        generatedPrompt.value = promptGenerator.generatePrompt({
          ...settings,
          customPrompt
        })

        const outputs = promptGenerator.generateTokenizedOutputs(generatedPrompt.value)
        tokenizedOutputs.t5xxl = outputs.t5xxl
        tokenizedOutputs.clipL = outputs.clipL
        tokenizedOutputs.clipG = outputs.clipG
        showTokenizedOutputs.value = true

        toast.add({ severity: 'success', summary: 'Generated', detail: 'Prompt generated successfully', life: 3000 })
      } catch (error) {
        toast.add({ severity: 'error', summary: 'Error', detail: 'Failed to generate prompt', life: 5000 })
      } finally {
        generating.value = false
      }
    }

    const enhancePrompt = async () => {
      if (!generatedPrompt.value) return

      enhancing.value = true
      try {
        enhancedPrompt.value = await apiService.enhancePrompt(
          generatedPrompt.value,
          enhancementSettings
        )
        toast.add({ severity: 'success', summary: 'Enhanced', detail: 'Prompt enhanced with AI', life: 3000 })
      } catch (error) {
        toast.add({ severity: 'error', summary: 'Error', detail: 'Failed to enhance prompt', life: 5000 })
      } finally {
        enhancing.value = false
      }
    }

    const onImageSelect = async (event) => {
      const file = event.files[0]
      if (!file) return

      // Create preview
      const reader = new FileReader()
      reader.onload = (e) => {
        uploadedImage.value = e.target.result
      }
      reader.readAsDataURL(file)

      // Generate caption
      try {
        generatedCaption.value = await apiService.generateCaption(file)
        toast.add({ severity: 'success', summary: 'Caption Generated', detail: 'Image caption generated successfully', life: 3000 })
      } catch (error) {
        toast.add({ severity: 'error', summary: 'Error', detail: 'Failed to generate caption', life: 5000 })
      }
    }

    const useCaption = () => {
      settings.customPrompt = generatedCaption.value
      toast.add({ severity: 'info', summary: 'Caption Used', detail: 'Caption copied to custom prompt', life: 2000 })
    }

    const copyPrompt = () => {
      navigator.clipboard.writeText(generatedPrompt.value)
      toast.add({ severity: 'info', summary: 'Copied', detail: 'Prompt copied to clipboard', life: 2000 })
    }

    const copyEnhancedPrompt = () => {
      navigator.clipboard.writeText(enhancedPrompt.value)
      toast.add({ severity: 'info', summary: 'Copied', detail: 'Enhanced prompt copied to clipboard', life: 2000 })
    }

    onMounted(async () => {
      await loadData()
      await checkOpenAI()
    })

    return {
      settings,
      enhancementSettings,
      dropdownOptions,
      compressionLevels,
      generating,
      enhancing,
      openaiAvailable,
      uploadedImage,
      generatedCaption,
      generatedPrompt,
      enhancedPrompt,
      tokenizedOutputs,
      showTokenizedOutputs,
      generatePrompt,
      enhancePrompt,
      onImageSelect,
      useCaption,
      copyPrompt,
      copyEnhancedPrompt
    }
  }
}
</script>

<style scoped>
.container {
  max-width: 1400px;
}
</style>
