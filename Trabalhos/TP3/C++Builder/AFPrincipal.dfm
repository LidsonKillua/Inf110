object frmPrincipal: TfrmPrincipal
  Left = 0
  Top = 0
  Caption = 'Aplicador de Filtros - Lidson Oliveira'
  ClientHeight = 380
  ClientWidth = 539
  Color = clBtnFace
  Font.Charset = DEFAULT_CHARSET
  Font.Color = clWindowText
  Font.Height = -12
  Font.Name = 'Segoe UI'
  Font.Style = []
  OnShow = FormShow
  TextHeight = 15
  object mmoPrincipal: TMemo
    Left = 0
    Top = 0
    Width = 539
    Height = 257
    Align = alTop
    ReadOnly = True
    TabOrder = 0
    ExplicitLeft = 8
  end
  object panButtons: TPanel
    Left = 0
    Top = 329
    Width = 539
    Height = 51
    Align = alClient
    TabOrder = 1
    ExplicitLeft = 272
    ExplicitTop = 320
    ExplicitWidth = 185
    ExplicitHeight = 41
    object btnImg: TButton
      Left = 16
      Top = 14
      Width = 113
      Height = 25
      Caption = 'Carregar Imagem'
      TabOrder = 0
      OnClick = btnImgClick
    end
    object btnAplicar: TButton
      Left = 147
      Top = 14
      Width = 113
      Height = 25
      Caption = 'Aplicar Filtro'
      TabOrder = 1
      OnClick = btnAplicarClick
    end
    object btnSalvar: TButton
      Left = 278
      Top = 14
      Width = 113
      Height = 25
      Caption = 'Salvar Imagem'
      TabOrder = 2
      OnClick = btnSalvarClick
    end
    object btnMostrar: TButton
      Left = 410
      Top = 14
      Width = 113
      Height = 25
      Caption = 'Mostrar Imagem'
      TabOrder = 3
      OnClick = btnMostrarClick
    end
  end
  object panFiltros: TPanel
    Left = 0
    Top = 257
    Width = 539
    Height = 72
    Align = alTop
    TabOrder = 2
    object rgrFiltros: TRadioGroup
      Left = 1
      Top = 1
      Width = 537
      Height = 70
      Align = alClient
      Caption = 'Filtros'
      Columns = 3
      ItemIndex = 0
      Items.Strings = (
        'Escurecer'
        'Clarear '
        'Negativo'
        'Espelhar'
        'Realce'
        'Filtro de Sobel'
        'Embossing'
        'Luminancia Vermelha'
        'Tons de cinza')
      TabOrder = 0
      ExplicitLeft = 88
      ExplicitTop = 48
      ExplicitWidth = 185
      ExplicitHeight = 105
    end
  end
  object opdPrincipal: TOpenPictureDialog
    Left = 208
    Top = 128
  end
  object spdPrincipal: TSavePictureDialog
    Left = 312
    Top = 128
  end
end
