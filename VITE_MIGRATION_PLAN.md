# Vite Migration Plan for Carbon Button Component

## Why Migrate?

Create React App (CRA) is being sunset as of 2025. The React team recommends:
- **Vite** for single-page apps (perfect for Streamlit components)
- **Next.js** for full-stack apps (overkill for components)

## Vite Advantages

1. **Faster builds** - 10-100x faster than CRA
2. **Smaller bundles** - Better tree-shaking
3. **No ejecting** - Full control without complexity
4. **Future-proof** - Actively maintained
5. **TypeScript built-in** - Zero config

## Migration Steps

### 1. Create Vite Project Structure

```bash
# In a new directory
npm create vite@latest carbon-button-vite -- --template react-ts
cd carbon-button-vite
npm install
```

### 2. Install Streamlit Component Library

```bash
npm install streamlit-component-lib
```

### 3. Vite Configuration

Create `vite.config.ts`:
```typescript
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],
  base: './',
  build: {
    outDir: '../briquette/frontend',
    emptyOutDir: true,
    rollupOptions: {
      output: {
        entryFileNames: 'static/js/[name].js',
        chunkFileNames: 'static/js/[name].js',
        assetFileNames: (assetInfo) => {
          if (assetInfo.name?.endsWith('.css')) {
            return 'static/css/[name][extname]'
          }
          return 'static/[ext]/[name][extname]'
        }
      }
    }
  }
})
```

### 4. Update package.json Scripts

```json
{
  "scripts": {
    "dev": "vite",
    "build": "vite build",
    "preview": "vite preview"
  }
}
```

### 5. Port Component Code

Copy existing component with minimal changes:
- Move `CarbonButton.tsx` to `src/`
- Update imports for Vite
- Keep same component logic

### 6. Build Output Structure

Vite output will be cleaner:
```
briquette/frontend/
├── index.html
└── static/
    ├── js/
    │   └── index.js (single file!)
    └── css/
        └── index.css
```

## Parallel Development Strategy

### Phase 1: Keep Both (Now)
```
carbon-button-component/
├── frontend/           # Current CRA version
├── frontend-vite/      # New Vite version
└── briquette/         # Can switch between builds
```

### Phase 2: Test Vite (Next Month)
- Build with Vite
- Test in development
- Compare bundle sizes
- Verify all features work

### Phase 3: Switch (When Confident)
- Replace CRA with Vite
- Update build scripts
- Archive CRA version

## Quick Start Commands

```bash
# Create Vite version alongside current
mkdir frontend-vite
cd frontend-vite
npm create vite@latest . -- --template react-ts
npm install
npm install streamlit-component-lib

# Copy component files
cp ../frontend/src/CarbonButton.tsx src/
cp ../frontend/src/index.tsx src/main.tsx
cp ../frontend/src/index.css src/

# Build
npm run build
```

## Risk Mitigation

1. **Keep CRA version working** until Vite is proven
2. **Test thoroughly** before switching
3. **Document differences** if any
4. **Maintain same API** for Python side

This way, you're prepared for the future without breaking what works today!