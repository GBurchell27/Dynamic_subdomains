# Multi-Tenant SaaS Platform with Dynamic Subdomains

This project is a multi-tenant SaaS platform where each client has their own dynamic subdomain (e.g., `clientA.yourapp.com`), customized branding, and potentially unique feature sets.

## Revised File Structure (with Next.js App Router)

```
my-multitenant-app/
├─ frontend/
│  ├─ app/                          # App Router structure
│  │  ├─ (auth)/                    # Route group for auth-related pages
│  │  │  ├─ login/
│  │  │  │  └─ page.tsx
│  │  │  └─ register/
│  │  │     └─ page.tsx
│  │  ├─ api/                       # API routes
│  │  │  ├─ tenants/
│  │  │  │  └─ route.ts
│  │  │  └─ auth/
│  │  │     └─ route.ts
│  │  ├─ dashboard/                 # Dashboard pages
│  │  │  └─ page.tsx
│  │  ├─ layout.tsx                 # Root layout (applies to all routes)
│  │  ├─ tenant-layout.tsx          # Tenant-specific layout
│  │  └─ page.tsx                   # Home page
│  ├─ components/
│  │  ├─ ui/                        # Reusable UI components
│  │  │  ├─ Navbar.tsx
│  │  │  ├─ Footer.tsx
│  │  │  └─ ...
│  │  └─ tenant/                    # Tenant-specific components
│  │     ├─ TenantHeader.tsx
│  │     └─ ...
│  ├─ lib/
│  │  ├─ tenant/                    # Tenant utilities
│  │  │  ├─ getTenantInfo.ts
│  │  │  └─ ...
│  │  └─ api.ts                     # API client utilities
│  ├─ middleware.ts                 # Handles subdomain routing & tenant context
│  ├─ public/
│  │  └─ tenant-logos/              # Tenant-specific assets
│  ├─ next.config.js
│  ├─ tailwind.config.js
│  └─ package.json
├─ backend/
│  ├─ app/
│  │  ├─ main.py                    # FastAPI entry point
│  │  ├─ routers/
│  │  │  ├─ tenant.py
│  │  │  ├─ auth.py
│  │  │  └─ ...
│  │  ├─ models/
│  │  │  ├─ tenant.py
│  │  │  └─ ...
│  │  ├─ schemas/
│  │  │  ├─ tenant.py
│  │  │  └─ ...
│  │  └─ core/
│  │     ├─ config.py               # DB connections, environment vars
│  │     └─ security.py
│  ├─ requirements.txt
│  └─ Dockerfile
├─ database/
│  ├─ migrations/
│  └─ init.sql
├─ docker/
│  ├─ docker-compose.yml
│  └─ ...
├─ .env.example
└─ README.md
```

## Key Differences with App Router Approach

- Uses Next.js App Router (`app/` directory) for enhanced routing capabilities
- Leverages route groups for better organization
- Implements middleware for tenant identification via subdomains
- Centralizes tenant-specific utilities in a dedicated lib folder
- Utilizes nested layouts for tenant-specific UI customization 