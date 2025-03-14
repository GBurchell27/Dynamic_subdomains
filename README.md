# Multi-Tenant SaaS Marketing Analytics Platform

This project is a multi-tenant SaaS platform where each client has their own dynamic subdomain (e.g., `clientA.yourapp.com`), customized branding, and tailored feature sets. The platform specifically focuses on delivering marketing analytics and Marketing Mix Modeling (MMM) capabilities as a service.

## Overview

The platform enables:

- **Dynamic Subdomains**: Each client accesses their custom-branded experience through their own subdomain
- **White-label Branding**: Tenants have personalized branding, colors, logos, and customized features
- **Unified Codebase**: A single codebase powers all tenant experiences, reducing maintenance overhead
- **Marketing Mix Modeling**: Specialized MMM analytics help clients understand marketing effectiveness
- **Flexible User Permissions**: Tenant administrators can manage their users' access to specific features and data

## Tech Stack

### Frontend
- **Language**: TypeScript (React)
- **Framework**: Next.js with App Router
- **Styling**: Tailwind CSS
- **UI library**: shadcn UI components, Lucide Icons

### Backend
- **Platform**: Supabase (provides PostgreSQL, Auth, Storage, APIs)
- **Authentication**: Supabase Auth with tenant context
- **Data Access**: Supabase client libraries with Row-Level Security
- **Serverless Functions**: Supabase Edge Functions for custom logic
- **API Framework**: FastAPI for advanced operations
- **AI Integration**: Pydantic AI (langchain as backup)
- **Caching**: Application-level caching with LRU cache pattern

### DevOps/Infrastructure
- Docker for containerization
- Docker Compose for local multi-service development
- AWS-based deployment (Route 53, CloudFront, ECS, etc.)

## Architecture

### Multi-Tenant Approach
Our system implements a secure multi-tenant architecture where:

1. **Tenant Identification**: Subdomains (e.g., `clientA.yourapp.com`) identify tenants
2. **Data Isolation**: Complete separation through Row-Level Security in PostgreSQL
3. **UI Customization**: Dynamic theming based on tenant configuration
4. **Feature Management**: Tenant-specific feature flags control available functionality

### Deployment Architecture
The platform uses an AWS-based deployment architecture:

```
Client Request (clientA.yourapp.com)
           ↓
    [AWS Route 53] 
           ↓                                    
  [CloudFront CDN] ←─── [S3 Buckets]            
           ↓            (Static Assets)         
[Application Load Balancer]                     
     ↙          ↘                               
[Next.js App]  [FastAPI Service]                
     ↓              ↓                           
[Supabase] ←─────── ↓                           
(Auth/DB)     [Elastic Cache]                   
     ↓        (Redis - Caching)                 
[S3 Storage]
(Tenant Assets)
```

## File Structure

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
│  │  │  ├─ webhooks/               # Webhook handlers (e.g., for Supabase events)
│  │  │  │  └─ route.ts
│  │  │  └─ tenant-admin/           # Admin-only API endpoints
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
│  │  ├─ supabase/                  # Supabase integration
│  │  │  ├─ client.ts               # Supabase client configuration
│  │  │  ├─ auth.ts                 # Authentication helpers with tenant context
│  │  │  └─ db-types.ts             # TypeScript types generated from Supabase schema
│  │  ├─ tenant/                    # Tenant utilities
│  │  │  ├─ getTenantInfo.ts
│  │  │  └─ theme.ts                # Tenant theme utilities
│  │  └─ utils/                     # General utilities
│  │     ├─ api.ts                  # API client utilities
│  │     └─ caching.ts              # Client-side caching utilities
│  ├─ middleware.ts                 # Handles subdomain routing & tenant context
│  ├─ public/
│  │  └─ tenant-assets/             # Default tenant assets
│  ├─ next.config.js
│  ├─ tailwind.config.js
│  └─ package.json
├─ backend/
│  ├─ supabase/                     # Supabase-specific code
│  │  ├─ functions/                 # Supabase Edge Functions
│  │  │  ├─ tenant-api/             # Tenant-specific API endpoints
│  │  │  │  └─ index.ts
│  │  │  └─ admin-api/              # Admin-only endpoints
│  │  │     └─ index.ts
│  │  ├─ migrations/                # SQL migrations for Supabase
│  │  │  ├─ 20230101_initial_schema.sql
│  │  │  └─ 20230102_tenant_policies.sql
│  │  ├─ seed/                      # Seed data for development
│  │  │  └─ demo_tenants.sql
│  │  └─ triggers/                  # Database triggers and functions
│  │     └─ tenant_functions.sql
│  ├─ app/                          # FastAPI app (for non-Supabase functionality)
│  │  ├─ main.py                    # FastAPI entry point
│  │  ├─ routers/                   # API routes
│  │  │  ├─ ai/                     # AI/ML integration endpoints
│  │  │  │  └─ mmm.py               # Marketing Mix Modeling endpoints
│  │  │  └─ analytics/              # Analytics endpoints
│  │  ├─ services/                  # Business logic
│  │  │  ├─ ai_service.py           # AI/ML service
│  │  │  └─ tenant_service.py       # Tenant management service
│  │  └─ core/
│  │     ├─ config.py               # Configuration (env vars, etc.)
│  │     └─ security.py             # Security utilities
│  ├─ requirements.txt
│  └─ Dockerfile
├─ docker/
│  ├─ docker-compose.yml            # Local development setup
│  ├─ docker-compose.prod.yml       # Production configuration
│  └─ ...
├─ .github/                         # CI/CD workflows
│  └─ workflows/
│     ├─ deploy-frontend.yml
│     └─ deploy-backend.yml
├─ .env.example                     # Template for environment variables
└─ README.md
```

## Key Features

### User Journey

1. **Public Landing Page (`yourapp.com`)**
   - Modern, responsive design with clear product information
   - Value proposition for marketing analytics platform
   - Call-to-Action buttons for "Request Demo" and "Login"

2. **Authentication Flow**
   - Direct login via `yourapp.com/login`
   - Subdomain access through `tenant.yourapp.com`
   - Optional SSO integration for enterprise tenants

3. **Tenant Dashboard**
   - Branded experience with tenant's colors, logo, and styling
   - Marketing Analytics Overview with performance metrics
   - MMM Insights with attribution modeling and recommendations
   - Report generation and export capabilities

4. **Admin Portal**
   - Tenant onboarding and management
   - User management with role-based permissions
   - System configuration and monitoring

5. **MMM Implementation**
   - Data ingestion from marketing platforms
   - Model building with customizable parameters
   - Interactive visualizations and reporting
   - Scenario planning and forecasting tools

## Security Considerations

- **Tenant Isolation**: Complete data separation through Row-Level Security
- **Authentication**: JWT tokens with tenant context
- **Authorization**: Fine-grained permissions based on user roles
- **Data Protection**: Encryption at rest for sensitive information
- **Audit Logging**: Comprehensive tracking of system access and changes

## Getting Started

Please refer to the documentation in the `.docs` directory for detailed setup instructions.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details. 